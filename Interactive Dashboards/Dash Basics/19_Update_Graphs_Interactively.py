import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

app = dash.Dash()

df = pd.read_csv('data/mpg.csv')

df['model_year'] = df['model_year'] + 1900

# we will add jitter to avoid straight lines of points.
df['model_year'] = np.random.randint(-5,5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div([
            html.Div([
                dcc.Graph(
                    id = 'mpg_scatter',
                    figure = {
                        'data':[go.Scatter(
                            x = df['model_year'],
                            y = df['mpg'],
                            text = df['name'],
                            hoverinfo = 'text',
                            mode = 'markers'
                        )],
                        'layout':go.Layout(
                            title = 'MPG Dataset',
                            xaxis = {'title':'model year'},
                            yaxis = {'title': 'miles per gallon'},
                            hovermode = 'closest'
                        )
                    }
                )], style = {'width': '70%', 'display':'inline-block'}),
                html.Div([
                    dcc.Graph(
                        id = 'mpg_line',
                        figure = {
                            'data':[go.Scatter(
                                x = [0,1],
                                y = [0,1],
                                mode = 'lines'
                            )],
                            'layout': go.Layout(
                                title = 'acceleration',
                                margin = {'l':0}
                            )
                        }
                    ),
                dcc.Markdown(
                    id='mpg_stats'
                    )
                ], style={'width':'30%', 'height':'60%','display':'inline-block'})
])

@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {
        'data': [go.Scatter(
            x = [0,1],
            y = [0, 60/df.iloc[v_index]['acceleration']],
            mode = 'lines',
            line = {'width': 2*df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible':True},
            yaxis = {'visible':True, 'range':[0,60/df['acceleration'].min()]},
            margin = {'l':0},
            height = 300
        )
    }
    return fig

@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
        {} cylinders
        {}cc displacement
        0 to 60mph in {} seconds
        """.format(df.iloc[v_index]['cylinders'],
            df.iloc[v_index]['displacement'],
            df.iloc[v_index]['acceleration'])
    return stats

if __name__ == '__main__':
    app.run_server()


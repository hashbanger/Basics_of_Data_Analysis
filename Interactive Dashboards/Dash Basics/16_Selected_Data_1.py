import dash 
import dash_html_components as html 
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json 

app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

app.layout = html.Div([
                html.Div([
                    dcc.Graph(
                        id = 'wheels-plot',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = df['color'],
                                    y = df['wheels'],
                                    dy = 1,
                                    mode = 'markers',
                                    marker = {
                                            'size': 15,
                                            'color': 'rgb(51,204,153)',
                                            'line': {'width': 2}
                                            }
                                        )
                                        ],
                            'layout': go.Layout(
                                            title = 'Wheels & Colors Scatterplot',
                                            xaxis = {'title': 'Color'},
                                            yaxis = {'title': '# of Wheels','nticks':3},
                                            hovermode = 'closest'
                                            )
                                    }
                            )], style = {'width':'40%', 'float': 'left'}),
                
                            html.Div([  
                                html.Pre(
                                    id = 'selection',
                                    style = {'width': '30%', 'display': 'inline-block'})
                                    ],
                                style = {'paddingTop': 35}),
])

@app.callback(Output('selection', 'children'),
            [Input('wheels-plot','selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent= 2)

if __name__ == '__main__':
    app.run_server()
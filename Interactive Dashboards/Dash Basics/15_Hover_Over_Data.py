import dash 
import dash_html_components as html 
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json 
import base64

app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

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
                                html.Img(
                                    id= 'hover-image', 
                                    src = 'children', 
                                    height = 300)
                                    ],
                                style = {'paddingTop': 35}),
])

@app.callback(Output('hover-image', 'src'),
            [Input('wheels-plot','hoverData')])
def callback_image(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path  = 'data/images/'
    return encode_image(path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])

# For changing the switching method to click rather than hover 
# replace hoverData with clickData

if __name__ == '__main__':
    app.run_server()
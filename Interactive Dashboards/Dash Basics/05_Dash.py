import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np 
import pandas as pd
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go 

app = dash.Dash()

df = pd.read_csv('OldFaithful.csv')

app.layout = html.Div(children = [
            html.H1('Welcome to Dash',
            style = {'textAlign': 'centre',
                    'color': '#111111'
                }
            ),

            dcc.Graph(
            id ='Scatter Plot',
            figure = {
                'data':[
                    go.Scatter(
                    x= df['Y'],
                    y = df['X'],
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(0, 138, 230)',
                        'line':{'width': 2}
                    }
                    )],
            'layout':go.Layout(title = 'Old Faithful Geyser Data',
                              xaxis = {'title': 'Waiting Time'},
                              yaxis = {'title': 'Eruptions'})}
            )])


if __name__ == '__main__':
    app.run_server()
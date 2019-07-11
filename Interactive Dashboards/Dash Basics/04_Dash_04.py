import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np 
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go 

app = dash.Dash()

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div(children = [
            html.H1('A Python Dash',
            style = {'textAlign': 'centre',
                    'color': '#111111'
                }
            ),

            dcc.Graph(
            id ='Scatter Plot 1',
            figure = {
                'data':[
                    go.Scatter(
                    x= random_x,
                    y = random_y,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51, 204, 153)',
                        'symbol':'pentagon',
                        'line':{'width': 2}
                    }
                    )],
            'layout':go.Layout(title = 'Random Data Plot 1',
                              xaxis = {'title': 'Some X title'})}
            ),
                        dcc.Graph(
            id ='Scatter Plot 2',
            figure = {
                'data':[
                    go.Scatter(
                    x= random_x,
                    y = random_y,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(200, 204, 153)',
                        'symbol':'pentagon',
                        'line':{'width': 2}
                    }
                    )],
            'layout':go.Layout(title = 'Random Data Plot 2',
                              xaxis = {'title': 'Some X title'})}
            )])


if __name__ == '__main__':
    app.run_server()
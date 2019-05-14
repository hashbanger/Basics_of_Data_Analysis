import dash
import dash_core_components as dcc
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(children = [
            html.H1('Hello Dash!'),
            html.Div('Dash: Dashboards in python'),
            dcc.Graph(id = 'Example Plot',
            figure =  {'data': [
            {'x':[1, 2, 3], 'y': [4, 1, 2], 'type':'bar', 'name':'Maharashtra'},
            {'x':[1, 2, 3], 'y': [4, 1, 2], 'type':'bar', 'name':'Delhi'}
            ],
            'layout':{
                'title':'BAR PLOTS!'
            }})
])

if __name__=='__main__':
    app.run_server()  
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# creating a dictionary for colours as we need
# to reference colour codes at several places
colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children = [
            html.H1('Hello Dash',
            style = {'textAlign': 'centre',
                    'color': colors['text']
                }
            ),

            dcc.Graph(
            id ='example plot',
            figure = {
                'data':[
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Mumbai'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Delhi'}
            ],
            'layout':{
            'plot_bgcolor': colors['background'],
            'paper_bgcolor':colors['background'],
            'font':{
                'color': colors['text']
                },
            'title': 'BAR PLOTS!'
            }
        }
    )],
    style = {'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server()

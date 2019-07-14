import dash 
import dash_html_components as html 
from dash.dependencies import Input, Output
import dash_core_components as dcc 

app = dash.Dash()

app.layout = html.Div([
            html.H1(id = 'live-update'),
            dcc.Interval(
                id = 'interval-component',
                interval = 1000,
                n_intervals = 0
            )
])

@app.callback(Output('live-update', 'children'),
            [Input('interval-component', 'n_intervals')])
def update_layout(n):
    return 'The page is refreshed %d times' %n
if __name__ == '__main__':
    app.run_server()
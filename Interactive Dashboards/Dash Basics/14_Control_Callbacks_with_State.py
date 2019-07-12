import dash 
import dash_core_components as dcc  
import dash_html_components as html 
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
                    dcc.Input(id = 'number-in', value = 'Hola! Amigos!', style = {'fontSize': 21}),
                    html.Button(id = 'submit-button',
                                n_clicks = 0,
                                children = 'Submit Here',
                                style = {'fontSize': 18}),
                    html.H2(id = 'number-out')        
])

@app.callback(Output('number-out','children'),
            [Input('submit-button','n_clicks')],
            [State('number-in','value')])
def output(n_clicks, number):
    return 'The above box says {} and the button was clicked {} times.'.format(number, n_clicks)

if __name__ == '__main__':
    app.run_server()
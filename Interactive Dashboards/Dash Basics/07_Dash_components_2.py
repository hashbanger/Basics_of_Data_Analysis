import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([

                    html.P(''),
                    html.Label('Dropdown'),
                    dcc.Dropdown(options =[{'label': 'NewDelhi', 'value': 'DEL'},
                                            {'label': 'Mumbai', 'value': 'MUM'}],
                                            value = 'DEL'),
                    html.P(''),
                    html.Label('Slider'),
                    dcc.Slider(min = -10, max = 10, step = 0.5, value = 0,
                                marks = {i: i for i in range(-10, 10, 1)})                    

])

if __name__ == '__main__':
    app.run_server()
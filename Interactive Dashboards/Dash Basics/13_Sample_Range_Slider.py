import dash 
import dash_html_components as html 
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import pandas as pd         

app = dash.Dash()

app.layout = html.Div([
                    dcc.RangeSlider(id = 'range-slider',
                        marks={i: str(i) for i in range(-5, 6)},
                        min=-5,
                        max=5,
                        value=[-1, 1]
                        ),
                    html.H1(id = 'product')
], style={'width':'100%'})

@app.callback(Output('product','children'),
                [Input('range-slider','value')])
def update_value(value_list):
    return value_list[0] * value_list[1]

if __name__ == '__main__':
    app.run_server()    
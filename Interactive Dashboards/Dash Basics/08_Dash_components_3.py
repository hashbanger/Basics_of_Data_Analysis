import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

Markdown_text = '''This is how you write a freaking markdown. There are pretty good sites for Data Science like [AnalyticsVidhya](https://www.analyticsvihya.com) 
                    many more.  
                    Do checkout my [GitHub](https://www.github.com/hashbanger)'''
app.layout = html.Div([dcc.Markdown(children = Markdown_text)])

if __name__ == '__main__':
    app.run_server()
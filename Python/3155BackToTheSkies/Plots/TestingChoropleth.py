import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    dcc.Graph(figure={'data': data_most_bizz,
                      'layout': go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                          xaxis={'title': 'Country'},
                                          yaxis={'title': 'Number of cases'}, barmode='stack')
                      })
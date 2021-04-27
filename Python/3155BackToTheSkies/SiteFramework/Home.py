import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
        # Header
        dbc.Row(children=[
                dbc.Col(html.Div(html.H1("Back to the Skies")), width=4),
                dbc.Col(html.Div(html.H2("COVID-19 Vaccination Data for Airline Travel")), width=8)
            ]),
        # Nav Buttons
        dbc.Row(children=[
                dbc.Col(html.Div(html.P("Point to Point")), width=4),
                dbc.Col(html.Div(html.P("See the Data")), width=4),
                dbc.Col(html.Div(html.P("About Us")), width=4)
            ])
    ]
)

if __name__ == "__main__":
    app.run_server()
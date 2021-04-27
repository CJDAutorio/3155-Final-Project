import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    # Header
    html.Div(children=[
        html.Div(
            dbc.Row(children=[
                dbc.Col(html.Div(html.H1("Back to the Skies")), width=4),
                dbc.Col(html.Div(html.H2("COVID-19 Vaccination Data for Airline Travel")), width="auto")
            ], align="start")
            ),
        # Nav Buttons
        dbc.Row(children=[
            dbc.Col(html.Div(html.A("Point to Point", href="https://www.google.com/")), width=4),
            dbc.Col(html.Div(html.A("See the Data", href="https://www.google.com/")), width=4),
            dbc.Col(html.Div(html.A("About Us", href="https://www.google.com/")), width=4)
        ], align="center")
    ])

])

if __name__ == "__main__":
    app.run_server()

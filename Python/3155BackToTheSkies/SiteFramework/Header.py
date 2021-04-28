import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


def getHeader():
    header = html.Div(children=[
        html.Div(children=[
            dbc.Row(children=[
                dbc.Col(html.Div(html.H1("Back to the Skies")))
            ]),
            dbc.Row(children=[
                dbc.Col(html.Div(html.H4("COVID-19 Vaccination Data for Airline Travel")))
            ], style={"font-weight": 400})],
            className="container-fluid"),

        # Nav Buttons
        dbc.NavbarSimple(children=[
            dbc.NavItem(
                dbc.NavLink("Point to Point", href="#", style={"padding-left": "10px", "padding-right": "10px"})),
            dbc.NavItem(dbc.NavLink("See the Data", href="#", style={"padding-left": "10px", "padding-right": "10px"})),
            dbc.NavItem(dbc.NavLink("About Us", href="#", style={"padding-left": "10px", "padding-right": "10px"}))
        ],
            brand="Back to the Skies",
            brand_href="#",
            color="primary",
            dark=True,
            style={"font-family": "'Inconsolata', monospace"})
    ], style={"padding-top": "1rem", "padding-bottom": "1rem"})

    return header

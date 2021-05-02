import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


def getHeader(title="Back to the Skies", subTitle="COVID-19 Vaccination Data for Airline Travel"):
    header = html.Div(children=[
        # Imports Google fonts
        html.Link(rel="preconnect", href="https://fonts.gstatic.com"),
        html.Link(rel="stylesheet",
                  href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@400;800&family=Open+Sans:wght@300;400&display=swap"),

        # Title and Subtitle
        html.Div(children=[
            dbc.Row(children=[
                dbc.Col(html.Div(html.H1(title)))
            ]),
            dbc.Row(children=[
                dbc.Col(html.Div(html.H4(subTitle)))
            ], style={"font-weight": 400})],
            className="container-fluid"),

        # Nav Buttons
        dbc.NavbarSimple(children=[
            dbc.NavItem(
                dbc.NavLink("FlySafe USA", href="/p2p", style={"padding-left": "10px", "padding-right": "10px"})),
            dbc.NavItem(dbc.NavLink("See the Data", href="/see_the_data",
                                    style={"padding-left": "10px", "padding-right": "10px"})),
            dbc.NavItem(dbc.NavLink("About Us", href="about_us", style={"padding-left": "10px", "padding-right": "10px"}))
        ],
            brand="Back to the Skies",
            brand_href="/",
            color="primary",
            dark=True,
            style={"font-family": "'Inconsolata', monospace"})
    ], style={"padding-top": "1rem", "padding-bottom": "1rem"})

    return header

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# external_stylesheets = [dbc.themes.BOOTSTRAP]
external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    # Imports Google fonts
    html.Link(rel="preconnect", href="https://fonts.gstatic.com"),
    html.Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@400;800&family=Open+Sans&display=swap"),

    # Header
    html.Div(children=[
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
    ], style={"padding-top": "1rem", "padding-bottom": "1rem"}),
    # Body
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(html.Div(style={"background-color": "#000000", "height": "500px", "width": "500px"}), width=6),
            dbc.Col(html.Div(children=[
                html.H3("Description"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            ]), width=6)
        ])
    ], className="container-fluid")
], className="container-xl")


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


def navbar():
    return -1


if __name__ == "__main__":
    app.run_server()

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#external_stylesheets = [dbc.themes.BOOTSTRAP]
external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    # Header
    html.Div(children=[
        html.Div(
            dbc.Row(children=[
                dbc.Col(html.Div(html.H1("Back to the Skies")), width="auto", className="homepageTitle"),
                dbc.Col(html.Div(html.H3("COVID-19 Vaccination Data for Airline Travel")), width="auto")
            ], align="start")
            , className="container-fluid"),
        # Nav Buttons
        dbc.Navbar(children=[
            dbc.Row(children=[
                html.A(dbc.Col("Point to Point"), href="#"),
                html.A(dbc.Col("See the Data"), href="#"),
                html.A(dbc.Col("About Us"), href="#")
            ])
        ],
            color="dark",
            dark=True)
    ]),
    # Body
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(html.Div(style={"background-color": "#000000", "height": "500px", "width": "500px"})),
            dbc.Col(html.Div(children=[
                html.H3("Description"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            ]))
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


if __name__ == "__main__":
    app.run_server()

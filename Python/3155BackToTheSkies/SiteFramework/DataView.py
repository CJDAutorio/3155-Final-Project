import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

# Sidebar for quickly changing graph type
sideBar = html.Div(children=[
    html.H3("Graphs"),
    dbc.Nav(children=[
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="#"), active="exact")
    ],
        vertical=True,
        pills=True)
])

# Actual graph content
content = html.Div(children=[

], className="container-fluid", style={"background-color": "#000000"})

app.layout = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dbc.Col(children=[
            sideBar
        ], style={"width": "2"}),
        dbc.Col(children=[
            content
        ]),
    ])
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

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

# Sidebar for quickly changing graph type
sideBar = dbc.Card(children=[
    html.H3("Graph Types"),
    html.H6("Change the type of graph"),
    # Changes graph data
    dbc.Nav(children=[
        dbc.NavItem(dbc.NavLink("Graph Type", href="/graph1"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="/graph2"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="/graph3"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="/graph4"), active="exact"),
        dbc.NavItem(dbc.NavLink("Graph Type", href="/graph5"), active="exact")
    ],
        vertical=True,
        pills=True)
])

# Actual graph content
content = html.Div(children=[

], className="container-fluid", style={"background-color": "#000000", "height": "100%"})

app.layout = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dbc.Col(children=[
            sideBar
        ], width=3),
        dbc.Col(children=[
            content
        ]),
    ])
], className="container-xl")


def getLayout():
    return app.layout


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


# Changes graph on button clicked
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("")
    elif pathname == "/graph1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/graph2":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/graph3":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/graph4":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/graph5":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server()

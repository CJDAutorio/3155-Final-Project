import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import ChartsMega as chm

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Sidebar with nav links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Test 1", href="/", active="exact"),
                dbc.NavLink("Test 2", href="/page-1", active="exact"),
                dbc.NavLink("Test 3", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dcc.Graph(figure=chm.bar1_most_vax())
    elif pathname == "/page-1":
        return dcc.Graph(figure=chm.bar2_least_vax())
    elif pathname == "/page-2":
        return dcc.Graph(figure=chm.sbar1_most_tour())


if __name__ == "__main__":
    app.run_server()
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    header.getHeader()
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
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header
import ChartsMega as chm

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout1 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.bar1_most_vax())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )

app.layout2 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.bar2_least_vax())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )

app.layout3 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.sbar1_most_bizz())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )

app.layout4 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.sbar2_most_tour())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )

app.layout5 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.choropleth1_USA())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )

app.layout6 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.choropleth1_USA())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
            "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
            "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    ])
], className="container-xl", )


def getLayout1():
    return app.layout1


def getLayout2():
    return app.layout2


def getLayout3():
    return app.layout3


def getLayout4():
    return app.layout4


def getLayout5():
    return app.layout5


def getLayout6():
    return app.layout6


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

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header


external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[

    # Header
    header.getHeader(),
    # Body
    html.Div(children=[
        # Jumbotron
        dbc.Row(children=[
            dbc.Jumbotron(children=[
                html.H2("Back to the Skies"),
                html.P("A solution for safer travelling during the COVID-19 Pandemic.", className="lead"),
                html.Hr(className="my-2"),
                html.P("Back to the Skies helps society slowly return to normalcy while staying as safe as possible "
                       "during this global pandemic by providing data on vaccinations in most possible travel "
                       "destinations. We hope to help promote airline travel to customers by providing an additional "
                       "sense of safety through comparative data.")
            ])
        ]),
        # Graph preview description
        dbc.Row(children=[
            dbc.Col(html.Div(children=[html.Img(src="https://via.placeholder.com/69"),
                                       html.P("PLACEHOLDER FOR GRAPH PREVIEW", style={"color": "#000000", "font-size": "4rem"})
                                       ], style={"height": "300px", "width": "500px"}), width=6),
            dbc.Col(html.Div(children=[
                html.H3("Description of Graphs"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                    "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
                    "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            ]), width=6)
        ])
    ], className="container-fluid")
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


if __name__ == "__main__":
    app.run_server()

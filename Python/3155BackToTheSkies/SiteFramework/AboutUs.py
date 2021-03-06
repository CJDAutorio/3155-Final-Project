import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)


def createCard(name="Placeholder", imageLink="https://via.placeholder.com/69",
               contList=["Placeholder", "Placeholder", "Placeholder"], ):
    contListHTML = []
    for i in contList:
        contListHTML.append(html.Li(i))

    card = dbc.Card(children=[
        dbc.CardHeader(html.H4(name)),
        dbc.CardImg(src=imageLink),
        dbc.CardBody(children=[
            html.H5("Contribution:"),
            html.Ul(children=contListHTML, className="card-text")
        ])
    ], style={"width": "15rem"})
    return card


app.layout = html.Div(children=[
    # Header
    header.getHeader(),
    # Body
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(name="Ben McDonald", imageLink="./assets/BenM.jpg", contList=["Product Contriver", "Dataset Collection", "Report Compilation"])
            ]),
            dbc.Col(children=[
                createCard(name="Ben Power", imageLink="./assets/Benp.jpg", contList=["Website Development", "Data Visualization", "Python Development"])
            ]),
            dbc.Col(children=[
                createCard(name="CJ D'Autorio", imageLink="./assets/cj_d.jpg", contList=["Website Layout", "Sketches", "Website Theme and Functionality"])
            ]),
            dbc.Col(children=[
                createCard(name="Eric Lynch", imageLink="./assets/Eric.jpg", contList=["Website Page Contents", "Presentation and Demo", "Sketches"])
            ]),
        ], className="container-fluid")
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


if __name__ == "__main__":
    app.run_server()

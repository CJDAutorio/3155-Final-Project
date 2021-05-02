import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]  # css stylesheet
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)


# card layout used for each data element on page
def createCard(cardTitle, cardText, cardButtonText, cardWidth="3", cardImage="https://via.placeholder.com/69",
               cardColor="primary", cardLink="#", cardSubtitle="Placeholder"):
    card = dbc.Card(children=[
        dbc.CardImg(src=cardImage, top=True),
        html.P(cardSubtitle, style={"font-size": "10px"}),
        dbc.CardBody([
            html.H4(cardTitle, className="card-title"),
            html.P(cardText, className="card-text"),
            dbc.Button(cardButtonText, color=cardColor, style={"font-family": "'Inconsolata', monospace"},
                       href=cardLink)
        ], style={"padding-top": "-10px"})
    ], style={"width": cardWidth})
    return card


# sets the layout of the page
app.layout = html.Div(children=[
    header.getHeader(),
    #
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(cardTitle="American Airlines", cardText="The safest places to vist ",
                           cardButtonText="Button",
                           cardLink="https://www.aa.com/homePage.do",
                           cardImage="./assets/pexels-karolina-grabowska-4047186.jpg",
                           cardSubtitle="Photo by Karolina Grabowska from Pexels")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="American Airlines",
                           cardText="Is it time to cancel your ticket?", cardButtonText="Button",
                           cardLink="/data_view2",
                           cardImage="./assets/pexels-pavel-danilyuk.jpg",
                           cardSubtitle="Photo by Pavel Danilyuk from Pexels")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="American Airlines",
                           cardText="Is it safe to do business overseas?", cardButtonText="Button",
                           cardLink="/data_view3",
                           cardImage="./assets/pexels-edmond-dantès-4342493.jpg",
                           cardSubtitle="Photo by Edmond Dantès from Pexels"),
            ], align="center", width=4)
        ], justify="around", style={"padding-bottom": "1rem"}),
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(cardTitle="American Airlines",
                           cardText="It's time to take the family back out!", cardButtonText="Button",
                           cardLink="/data_view4",
                           cardImage="./assets/pexels-jaxson-bryden-2040627.jpg",
                           cardSubtitle="Photo by Jaxson Bryden from Pexels")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="American Airlinese", cardText="Where in the USA is it the safest?",
                           cardButtonText="Button",
                           cardLink="/data_view5",
                           cardImage="./assets/pexels-cdc-3992931.jpg",
                           cardSubtitle="Photo by CDC from Pexels")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="American Airlines", cardText="How we are keeping you safe in the skies!",
                           cardButtonText="Button",
                           cardLink="/data_view6",
                           cardImage="./assets/pexels-august-de-richelieu-4261252.jpg",
                           cardSubtitle="Photo by August de Richelieu from Pexels")
            ], align="center", width=4)
        ], justify="around", style={"padding-bottom": "1rem"})
    ])
], className="container-xl")


# returns the layout
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

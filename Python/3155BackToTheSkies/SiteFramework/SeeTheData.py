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
               cardColor="primary", cardLink="#"):
    card = dbc.Card(children=[
        dbc.CardImg(src=cardImage, top=True),
        dbc.CardBody([
            html.H4(cardTitle, className="card-title"),
            html.P(cardText, className="card-text"),
            dbc.Button(cardButtonText, color=cardColor, style={"font-family": "'Inconsolata', monospace"},
                       href=cardLink)
        ])
    ], style={"width": cardWidth})
    return card


# sets the layout of the page
app.layout = html.Div(children=[
    header.getHeader(),
    #
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(cardTitle="Top Countries by Vaccinations per Capita", cardText="The safest places to vist "
                                                                                          "in the world...",
                           cardButtonText="Button",
                           cardLink="/data_view1")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="Worst Countries by Vaccinations per Capita",
                           cardText="Is it time to cancel your ticket!!??", cardButtonText="Button",
                           cardLink="/data_view2")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="Vaccination Data on Top Business Locations",
                           cardText="Is it safe to do business overseas?", cardButtonText="Button",
                           cardLink="/data_view3")
            ], align="center", width=4)
        ], justify="around", style={"padding-bottom": "1rem"}),
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(cardTitle="Vaccination Data on Top Vacation Locations",
                           cardText="Its time to take the family back out!", cardButtonText="Button",
                           cardLink="/data_view4")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="Vaccine Allocation by State", cardText="Where in the usa is it the safest?",
                           cardButtonText="Button",
                           cardLink="/data_view5")
            ], align="center", width=4),
            dbc.Col(children=[
                createCard(cardTitle="COVID-19 Procedures", cardText="How we are keeping you safe in the skies!",
                           cardButtonText="Button",
                           cardLink="/data_view6")
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

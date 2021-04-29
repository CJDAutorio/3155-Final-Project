import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)


def createCard(cardTitle, cardText, cardButtonText, cardWidth="18rem", cardImage="https://via.placeholder.com/150", cardColor="primary"):
    card = dbc.Card(children=[
        dbc.CardImg(src=cardImage, top=True),
        dbc.CardBody([
            html.H4(cardTitle, className="card-title"),
            html.P(cardText, className="card-text"),
            dbc.Button(cardButtonText, color=cardColor, style={"font-family": "'Inconsolata', monospace"})
        ])
    ], style={"width": cardWidth})
    return card


app.layout = html.Div(children=[
    header.getHeader(),
    #
    html.Div(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                createCard(cardTitle="Test Card", cardText="A test card's description.", cardButtonText="Button")
            ], width=4),
            dbc.Col(children=[
                createCard(cardTitle="Test Card", cardText="A test card's description.", cardButtonText="Button")
            ], width=4),
            dbc.Col(children=[
                createCard(cardTitle="Test Card", cardText="A test card's description.", cardButtonText="Button")
            ], width=4)
        ], justify="center")
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
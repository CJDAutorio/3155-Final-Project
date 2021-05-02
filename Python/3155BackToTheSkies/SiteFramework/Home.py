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
                html.H3("Travel Advisory Updates"),
                html.P(
                    "The COVID-19 pandemic continues to pose unprecedented risks to travelers. In light of those risks,"
                    " the Department of State strongly recommends U.S. citizens reconsider all travel abroad.\n "
                    "As travelers face ongoing risks due to the COVID-19 pandemic, the Department of State will begin "
                    "updating its Travel Advisories this week to better reflect the Centers for Disease Control and "
                    "Prevention’s (CDC) science-based Travel Health Notices that outline current issues affecting "
                    "travelers’ health. Our Advisories also take into account logistical factors, including in-country "
                    "testing availability and current travel restrictions for U.S. citizens. \n"
                    "This update will result in a significant increase in the number of countries at Level 4: Do Not "
                    "ravel, to approximately 80% of countries worldwide. This does not imply a reassessment of the "
                    "current health situation in a given country, but rather reflects an adjustment in the State "
                    "Department’s Travel Advisory system to rely more on CDC’s existing epidemiological assessments.")
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

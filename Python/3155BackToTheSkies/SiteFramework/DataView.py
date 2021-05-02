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
            "As vaccines continue to be distributed around the world and more of the population becomes vaccinated the risk of "
            "contracting and spreading Covid-19 will decrease, and the safer it will be to return to a state of normalcy. "
            "Covid-19's herd immunity threshold level is not yet known, however, most estimates have placed the threshold at 60% to 70%. "
            "The above bar chart displays the top 10 countries with the highest vaccination rates per capita around the world. "
            "Thus, with this data these countries can currently be considered some of the safest places to travel to.")
    ])
], className="container-xl", )

app.layout2 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.bar2_least_vax())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "The lower the percentage of vaccinated citizens within a population, the more at risk one would be for contracting Covid-19. "
            "This viral disease can spread between people, mainly through close contact, and those infected rarely show symptoms right away. "
            "Consequently, the infected may be spreading the disease without ever being aware that they contracted it themselves. "
            "The bar chart shown above displays the top 10 countries with the lowest vaccination rates per capita around the world. "
            "Thus, with this data, these countries can be considered some of the worst and most dangerous countries to travel to during the pandemic. " )
    ])
], className="container-xl", )

app.layout3 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.sbar1_most_bizz())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "Business travelers account for about 12% of all airline passengers and can account for up to 75% of airline profits. "
            "Additionally, some businesses must continue to operate throughout the Covid-19 pandemic and would like employees to be "
            "able to travel as soon as current local restrictions would allow them to. If you are planning on traveling for business, "
            "be sure to give our Covid-19 procedures page a view to see the procedures for some of the most popular airline companies. "
            "The stacked bar chart shown above displays how much of a population is completely unvaccinated, partially vaccinated, or "
            "fully vaccinated within the top 10 most traveled to business locations of the world.")
    ])
], className="container-xl", )

app.layout4 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.sbar2_most_tour())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "The list of places that’s welcoming vaccinated people is growing by the week."),
        html.P(
            "Proof of vaccines is easing travel restrictions to some places, and is the only way travelers can gain "
            "entrance to others."),
        html.P(
            "Yet from health forms to testing protocols, travel remains complicated even for the immunized. Rules "
            "differ from one country to the next. Some places reject certain types of vaccines, while "
            "others still require a quarantine period — often shortened."),
        html.P(
            "Travelers almost always have to be fully"
            " vaccinated — which is commonly defined as two weeks following the last required dose. However, several "
            "places allow travel the same day as a second shot."),
        html.P("So travelers should read the fine print before "
               "booking a trip abroad, which includes understanding Covid-19 protocols that may be stricter than "
               "what’s "
               "required at home."),
        html.Hr(),
        html.Hr()
    ])
], className="container-xl", )

app.layout5 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.choropleth1_USA())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "All adults in the U.S. are now eligible for a coronavirus vaccine. Vaccinations climbed to an average of"
            " more than 3.3 million shots per day before it began declining since then. The decline coincided with a"
            " pause in the use of the Johnson & Johnson coronavirus vaccine that began on on April 13 and lasted until"
            " April 23, as federal health officials reviewed reports of a rare and severe type of blood clot. "
            "Resumption "
            "of the J&J vaccine is seen as a key component of vaccine delivery because it requires only one dose "
            "instead "
            "of two. Lack of demand may also be contributing to the vaccine slowdown as adults who most want the shot "
            " have received it so the campaign must now reach out to more hesitant people.")
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

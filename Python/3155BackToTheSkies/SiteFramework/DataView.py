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
            "   The bar chart shown above displays the top 10 countries with the highest vaccination rate per capita around the world. "
            "Thus, with this data these countries can be considered some of the safest countries to travel to during this pandemic. " )
    ])
], className="container-xl", )

app.layout2 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.bar2_least_vax())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "The bar chart shown above displays the top 10 countries with the lowest vaccination rate per capita around the world. "
            "Thus, with this data these countries can be considered some of the worst and most dangerous countries to travel to during this pandemic. " )
    ])
], className="container-xl", )

app.layout3 = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dcc.Graph(figure=chm.sbar1_most_bizz())
    ], justify="center", style={"padding-bottom": "5%"}),
    dbc.Row(children=[
        html.P(
            "The stacked bar chart shown above displays how much of a population is completely unvaccinated, partially vaccinated, or fully vaccinated"
            "within the top 10 most traveled to business locations of the world.")
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
            "All adults in the U.S. are now eligible for a coronavirus vaccine. Vaccinations climbed to an average of"
            " more than 3.3 million shots per day before it began declining since then. The decline coincided with a"
            " pause in the use of the Johnson & Johnson coronavirus vaccine that began on on April 13 and lasted until"
            " April 23, as federal health officials reviewed reports of a rare and severe type of blood clot. "
            "Resumption "
            "of the J&J vaccine is seen as a key component of vaccine delivery because it requires only one dose "
            "instead "
            "of two.\nLack of demand may also be contributing to the vaccine slowdown as adults who most want the shot "
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

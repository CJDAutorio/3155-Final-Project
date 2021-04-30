import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# --------------------------------
# BAR CHART Most Vaccinated Countries
# --------------------------------

# Load CSV files from dataset folder
data1 = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')
data2 = pd.read_csv('../Datasets/vaccination-data.csv')

# --- Filtering data ---
dataVacPerCap = data2.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[False]).head(10)
dataVacPerCap = dataVacPerCap.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces

# --- Preparing data and layout ---
dataPer100 = [go.Bar(x=dataVacPerCap['COUNTRY'], y=dataVacPerCap['TOTAL_VACCINATIONS_PER100'] / 100)]
layoutPer100 = go.Layout(title="Most Vaccinated Counties", title_font_size=22, xaxis_title="Country",
                         yaxis_title="Percentage Vaccinated")
fig = go.Figure(data=dataPer100, layout=layoutPer100)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Sidebar with nav links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Test 1", href="/", active="exact"),
                dbc.NavLink("Test 2", href="/page-1", active="exact"),
                dbc.NavLink("Test 3", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content","children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dcc.Graph(figure=fig)
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")


if __name__ == "__main__":
    app.run_server()

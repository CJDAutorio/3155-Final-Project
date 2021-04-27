import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load CSV files from Dataset folder
data1 = pd.read_csv('../Datasets/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Moderna.csv')

# --------------------------------
# STACKED BAR CHART Most Tourism
# --------------------------------

app = dash.Dash()

# --- Filtering data ---
usa_data = data1
usa_data['Week of Allocations'] = pd.to_datetime(usa_data['Week of Allocations'])
usa_dataClean = usa_data.sort_values(by=['Week of Allocations'], ascending=[False]).head(10)

# --- Preparing data and layout ---
fig = px.choropleth(usa_dataClean, locations='Jurisdiction', locationmode='USA-states', color="1st Dose Allocations",
                    hover_name='Jurisdiction', projection="albers usa", title="temp",
                    color_continuous_scale=px.colors.sequential.Agsunset)

# --- Plot the figure and saving in a html file ---
app.layout = html.Div([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


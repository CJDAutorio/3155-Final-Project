import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load CSV files from Dataset folder
data1 = pd.read_csv('../Datasets/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_ModernaWOW.csv')

# --------------------------------
# STACKED BAR CHART Most Tourism
# --------------------------------

app = dash.Dash()

# --- Filtering data ---
usa_data = data1
usa_data['Week of Allocations'] = pd.to_datetime(usa_data['Week of Allocations'])
usa_dataClean = usa_data.sort_values(by=['Week of Allocations'], ascending=[False]).head(60)

state_codes = {
    'District of Columbia': 'dc', 'Mississippi': 'MS', 'Oklahoma': 'OK',
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR',
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA',
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ',
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT',
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT',
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV',
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND',
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY',
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH',
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD',
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA',
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX',
    'Nevada': 'NV', 'Maine': 'ME', 'Palau': 'RIP',"Federal Entities": 'RIP', 'Philadelphia': 'RIP', 'Chicago': 'RIP'}

# usa_dataClean['Jurisdiction'] = usa_dataClean[usa_dataClean['Jurisdiction'] == state_codes]
usa_dataClean = usa_dataClean.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces
usa_dataClean['Jurisdiction'] = usa_dataClean['Jurisdiction'].apply(lambda x: state_codes[x])

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


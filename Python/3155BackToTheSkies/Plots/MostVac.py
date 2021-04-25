import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV files from dataset folder
data1 = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')
data2 = pd.read_csv('../Datasets/vaccination-data.csv')

# --------------------------------
# STACKED BAR CHART Most Tourism
# --------------------------------

# --- Filtering data ---
country_code = ['ESP', 'USA', 'CHN', 'ITA', 'TUR', 'MEX', 'DEU', 'THA', 'GBR']
country_pop = [47, 328, 1398, 60, 82, 127, 83, 70, 67]

dataMostTourism = (data2[data2['ISO3'] == 'FRA'])

for x in country_code:
    dataMostTourism = dataMostTourism.append(data2[data2['ISO3'] == x])
dataMostTourism = dataMostTourism.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces

dataMostTourism = dataMostTourism.sort_values(by=['TOTAL_VACCINATIONS'], ascending=False)  # Sort by total vaccinations
dataMostTourism['FullVax'] = (dataMostTourism['TOTAL_VACCINATIONS'] - dataMostTourism['PERSONS_VACCINATED_1PLUS_DOSE'])


# --- Preparing data and layout ---
trace1_tourism = go.Bar(x=dataMostTourism['COUNTRY'], y=dataMostTourism['PERSONS_VACCINATED_1PLUS_DOSE'])
trace2_tourism = go.Bar(x=dataMostTourism['COUNTRY'], y=dataMostTourism['FullVax'])

data_most_tour = [trace1_tourism, trace1_tourism]
layout1 = go.Layout(title="Most Vaccinated Counties", title_font_size=22, xaxis_title="Country",
                    yaxis_title="Percentage Vaccinated")

# --- Plot the figure and saving in a html file ---
dcc.Graph

fig = go.Figure(data=data_most_tour, layout=layout1)
pyo.plot(fig, filename='barchart.html')



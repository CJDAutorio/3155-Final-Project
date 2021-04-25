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

# BAR CHART Most Vaccinated Countries
# --------------------------------
# Filtering data
dataVacPerCap = data2.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[False]).head(10)
dataVacPerCap = dataVacPerCap.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data and layout
dataPer100 = [go.Bar(x=dataVacPerCap['COUNTRY'], y=dataVacPerCap['TOTAL_VACCINATIONS_PER100'] / 100)]
layoutPer100 = go.Layout(title="Most Vaccinated Counties", title_font_size=22, xaxis_title="Country",
                         yaxis_title="Percentage Vaccinated")
# Plot the figure and saving in a html file
fig = go.Figure(data=dataPer100, layout=layoutPer100)
pyo.plot(fig, filename='VacPer100barchart.html')

# STACKED BAR CHART Most Tourism
# --------------------------------

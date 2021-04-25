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

# Filtering data
dataVacPerCap = data2.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[False]).head(10)

# Preparing data
dataPer100 = [go.Bar(x=dataVacPerCap['COUNTRY'], y=dataVacPerCap['TOTAL_VACCINATIONS_PER100'])]

# Preparing layout
layoutPer100 = go.Layout(title="Vac per 100", xaxis_title="Country", yaxis_title="Total per 100")

# Plot the figure and saving in a html file
fig = go.Figure(data=dataPer100, layout=layoutPer100)
pyo.plot(fig, filename='barchart.html')
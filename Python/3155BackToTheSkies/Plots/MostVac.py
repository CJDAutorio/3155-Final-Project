import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


# Load CSV files from dataset folder
data1 = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')

# Filtering data
data12 = data1[data1['New_deaths'] >= 5000]

# Preparing data
data = [go.Bar(x=data12['Date_reported'], y=data12['New_deaths'])]

# Preparing layout
layout = go.Layout(title='xyz', xaxis_title="zzz",
                   yaxis_title="yml")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')

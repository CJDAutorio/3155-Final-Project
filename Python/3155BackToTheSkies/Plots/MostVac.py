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


# Preparing layout


# Plot the figure and saving in a html file

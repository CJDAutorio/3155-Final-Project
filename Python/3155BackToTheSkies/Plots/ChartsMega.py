import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load CSV files from Dataset folder
data_covid_global = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')
data_vax_global = pd.read_csv('')
data_vax_usaDist = pd.read_csv('')

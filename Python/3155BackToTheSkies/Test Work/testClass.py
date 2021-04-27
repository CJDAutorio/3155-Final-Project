# test.py>
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


data1 = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')
data2 = pd.read_csv('../Datasets/vaccination-data.csv')

# --------------------------------
# BAR CHART Most Vaccinated Countries
# --------------------------------

# --- Filtering data ---
dataVacPerCap = data2.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[False]).head(10)
dataVacPerCap = dataVacPerCap.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces

# --- Preparing data and layout ---
dataPer100 = [go.Bar(x=dataVacPerCap['COUNTRY'], y=dataVacPerCap['TOTAL_VACCINATIONS_PER100'] / 100)]
layoutPer100 = go.Layout(title="Most Vaccinated Counties", title_font_size=22, xaxis_title="Country",
                         yaxis_title="Percentage Vaccinated")
# --- Plot the figure and saving in a html file ---
fig = go.Figure(data=dataPer100, layout=layoutPer100)


def returnFig():
    return fig

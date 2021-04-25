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

app = dash.Dash()
# --------------------------------
# STACKED BAR CHART Most Tourism
# --------------------------------

# --- Filtering data ---
country_code = ['ESP', 'USA', 'ITA', 'TUR', 'MEX', 'DEU', 'THA', 'GBR', 'JPN']
country_pop = [47, 328, 1398, 60, 82, 127, 83, 70, 67]

dataMostTourism = (data2[data2['ISO3'] == 'FRA'])

for x in country_code:
    dataMostTourism = dataMostTourism.append(data2[data2['ISO3'] == x])
dataMostTourism = dataMostTourism.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces

dataMostTourism = dataMostTourism.sort_values(by=['TOTAL_VACCINATIONS'], ascending=False)  # Sort by total vaccinations
dataMostTourism['FullVax'] = (dataMostTourism['TOTAL_VACCINATIONS'] - dataMostTourism['PERSONS_VACCINATED_1PLUS_DOSE'])

# --- Preparing data and layout ---
trace1_tourism = go.Bar(x=dataMostTourism['COUNTRY'], y=dataMostTourism['PERSONS_VACCINATED_1PLUS_DOSE'],
                        name='One Does')
trace2_tourism = go.Bar(x=dataMostTourism['COUNTRY'], y=dataMostTourism['FullVax'], name='full vax')
data_most_tour = [trace1_tourism, trace2_tourism]

# --- Plot the figure and saving in a html file ---
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    dcc.Graph(figure={'data': data_most_tour,
                      'layout': go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                          xaxis={'title': 'Country'},
                                          yaxis={'title': 'Number of cases'}, barmode='stack')
                      })

])

# pyo.plot(fig, filename='barchart.html')
if __name__ == '__main__':
    app.run_server()

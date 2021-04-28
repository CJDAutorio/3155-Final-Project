import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# --------------------------------
# STACKED BAR CHART Most Business Travel
# --------------------------------
data2 = pd.read_csv('../Datasets/vaccination-data.csv')
app = dash.Dash()
# --- Filtering data ---
country_code = ['IRL', 'USA', 'ITA', 'ESP', 'DOM', 'DEU', 'NLD', 'GBR', 'JPN']
dataMostBizz = (data2[data2['ISO3'] == 'FRA'])

for x in country_code:
    dataMostBizz = dataMostBizz.append(data2[data2['ISO3'] == x])


dataMostBizz['FullVax'] = (dataMostBizz['TOTAL_VACCINATIONS'] - dataMostBizz['PERSONS_VACCINATED_1PLUS_DOSE'])
# Calculates total pop from given info
dataMostBizz['Total Population'] = \
    (dataMostBizz['PERSONS_VACCINATED_1PLUS_DOSE']/(dataMostBizz['PERSONS_VACCINATED_1PLUS_DOSE_PER100']/100))
dataMostBizz['NoVax'] = dataMostBizz['Total Population'] - dataMostBizz['PERSONS_VACCINATED_1PLUS_DOSE']
dataMostBizz = dataMostBizz.sort_values(by=['Total Population'], ascending=False)

# --- Preparing data and layout ---
trace1 = go.Bar(x=dataMostBizz['COUNTRY'],y=dataMostBizz['NoVax'], name='No Vax')
trace2 = go.Bar(x=dataMostBizz['COUNTRY'],y=(dataMostBizz['PERSONS_VACCINATED_1PLUS_DOSE'] - dataMostBizz['FullVax']),
                name='Partial Vax')
trace3 = go.Bar(x=dataMostBizz['COUNTRY'],y=dataMostBizz['FullVax'], name='Full Vax')
data_most_bizz =[trace1, trace2, trace3]

lay = go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                          xaxis={'title': 'Country'},
                                          yaxis={'title': 'Number of cases'}, barmode='stack')
fig = go.Figure(data=data_most_bizz, layout=lay)
# --- Plot the figure and saving in a html file ---
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    dcc.Graph(figure={'data': data_most_bizz,
                      'layout': go.Layout(title='Corona Virus Cases in the first 20 country expect China',
                                          xaxis={'title': 'Country'},
                                          yaxis={'title': 'Number of cases'}, barmode='stack')
                      })

])

if __name__ == '__main__':
    app.run_server()


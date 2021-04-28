import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html

# --- Load CSV files from Dataset folder ---
data_covid_global = pd.read_csv('../Datasets/WHO-COVID-19-global-data.csv')
data_vax_global = pd.read_csv('../Datasets/vaccination-data.csv')
data_vax_usaDist = pd.read_csv('../Datasets/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_ModernaWOW.csv')


# --------------------------------
# BAR CHART Most Vaccinated Countries
# --------------------------------
def bar1_most_vax():

    # --- Filtering data ---
    # Sorts data by TOTAL_VACCINATIONS_PER100 then removes all but the top 10
    data_most_vax = data_vax_global.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[False]).head(10)
    # removes empty spaces from data
    data_most_vax = data_most_vax.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # --- Preparing data and layout ---
    # Sets the X axis to counties and the y axis to % vaccinated
    graph_most_vax = [go.Bar(x=data_most_vax['COUNTRY'], y=(data_most_vax['TOTAL_VACCINATIONS_PER100'] / 100))]
    # Sets the layout of the figure
    layout_most_vax = go.Layout(title="Highest Vaccinations Per 100", title_font_size=24, xaxis_title="Country",
                                yaxis_title="Percentage Vaccinated")

    # --- Plot the figure and return it ---
    fig = go.Figure(data=graph_most_vax, layout=layout_most_vax)  # figure used by dash to make chart
    return fig

# --------------------------------
# BAR CHART Least Vaccinated Countries
# --------------------------------
def bar2_least_vax():

    # --- Filtering data ---
    # removes countries that haven't started vaccinations
    data_least_vax = data_vax_global[data_vax_global['TOTAL_VACCINATIONS_PER100'] > 1]
    # Sorts data by TOTAL_VACCINATIONS_PER100 then removes all but the top 10
    data_least_vax = data_least_vax.sort_values(by=['TOTAL_VACCINATIONS_PER100'], ascending=[True]).head(10)
    # removes empty spaces from data
    data_least_vax = data_least_vax.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # --- Preparing data and layout ---
    # Sets the X axis to counties and the y axis to % vaccinated
    graph_least_vax = [go.Bar(x=data_least_vax['COUNTRY'], y=(data_least_vax['TOTAL_VACCINATIONS_PER100'] / 100))]
    # Sets the layout of the figure
    layout_least_vax = go.Layout(title="Lowest Vaccinations Per 100", title_font_size=24, xaxis_title="Country",
                                 yaxis_title="Percentage Vaccinated")

    # --- Plot the figure and return it ---
    fig = go.Figure(data=graph_least_vax, layout=layout_least_vax)  # figure used by dash to make chart
    return fig

# --------------------------------
# STACKED BAR CHART Most Tourism Vax Data
# --------------------------------
def sbar1_most_tour():

    # --- Filtering data ---
    country_code = ['ESP', 'USA', 'ITA', 'TUR', 'MEX', 'DEU', 'THA', 'GBR', 'JPN']
    data_most_tourism = data_vax_global[data_vax_global['ISO3'] == 'FRA']
    for x in country_code:
        data_most_tourism = data_most_tourism.append(data_vax_global[data_vax_global['ISO3'] == x])
    data_most_tourism = data_most_tourism.apply(lambda x: x.str.strip if x.dtype == "object" else x)


    # --- Preparing data and layout ---

    # --- Plot the figure and saving in a html file ---




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

# Dictionary to translate state names for choropleth maps
state_codes = {
    'District of Columbia': 'dc', 'Mississippi': 'MS', 'Oklahoma': 'OK',
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR',
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA',
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ',
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT',
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT',
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV',
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND',
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY',
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH',
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD',
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA',
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX',
    'Nevada': 'NV', 'Maine': 'ME', 'Palau': 'RIP', "Federal Entities": 'RIP', 'Philadelphia': 'RIP', 'Chicago': 'RIP'}


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
    data_least_vax = (data_vax_global[data_vax_global['TOTAL_VACCINATIONS_PER100'] > 1])
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
# STACKED BAR CHART Most Business Travel Vax Data
# --------------------------------
def sbar1_most_bizz():
    # --- Filtering data ---
    # List of countries to use for graph
    country_code = ['IRL', 'USA', 'ITA', 'ESP', 'DOM', 'DEU', 'NLD', 'GBR', 'JPN']
    # Creates dataFrame and adds first country
    data_most_bizz = (data_vax_global[data_vax_global['ISO3'] == 'FRA'])

    # adds countries from list to data frame using data_vax_global data
    for x in country_code:
        data_most_bizz = data_most_bizz.append(data_vax_global[data_vax_global['ISO3'] == x])

    # calculates total population fully vaccinated
    data_most_bizz['FullVax'] = (
            data_most_bizz['TOTAL_VACCINATIONS'] - data_most_bizz['PERSONS_VACCINATED_1PLUS_DOSE'])
    # Calculates total pop of country from given info(per 100 vaccinated and # people vaccinated)
    data_most_bizz['Total Population'] = \
        (data_most_bizz['PERSONS_VACCINATED_1PLUS_DOSE'] / (
                data_most_bizz['PERSONS_VACCINATED_1PLUS_DOSE_PER100'] / 100))
    # Calculates total population not at all vaccinated
    data_most_bizz['NoVax'] = (
            data_most_bizz['Total Population'] - data_most_bizz['PERSONS_VACCINATED_1PLUS_DOSE'])
    # sorts the data by population
    data_most_bizz = data_most_bizz.sort_values(by=['Total Population'], ascending=False)

    # --- Preparing data and layout ---
    # 3 trace's used for each stacking level of the bar chart
    trace1 = go.Bar(x=data_most_bizz['COUNTRY'], y=data_most_bizz['NoVax'], name='No Vax')
    trace2 = go.Bar(x=data_most_bizz['COUNTRY'],
                    y=(data_most_bizz['PERSONS_VACCINATED_1PLUS_DOSE'] - data_most_bizz['FullVax']),
                    name='Partial Vax')
    trace3 = go.Bar(x=data_most_bizz['COUNTRY'], y=data_most_bizz['FullVax'], name='Full Vax')
    # sets data for graph
    graph_most_bizz = [trace1, trace2, trace3]
    # sets layout for graph
    lay = go.Layout(title='Title Here',
                    xaxis={'title': 'Country'},
                    yaxis={'title': 'Population'}, barmode='stack')

    # --- Plot the figure and return it ---
    fig = go.Figure(data=graph_most_bizz, layout=lay)
    return fig


# --------------------------------
# STACKED BAR CHART Most Tourism Travel Vax Data
# --------------------------------
def sbar2_most_tour():
    # --- Filtering data ---
    # List of countries to use for graph
    country_code = ['ESP', 'USA', 'ITA', 'TUR', 'MEX', 'DEU', 'THA', 'GBR', 'JPN']
    # Creates dataFrame and adds first country
    data_most_tourism = (data_vax_global[data_vax_global['ISO3'] == 'FRA'])

    # adds countries from list to data frame using data_vax_global data
    for x in country_code:
        data_most_tourism = data_most_tourism.append(data_vax_global[data_vax_global['ISO3'] == x])

    # calculates total population fully vaccinated
    data_most_tourism['FullVax'] = (
            data_most_tourism['TOTAL_VACCINATIONS'] - data_most_tourism['PERSONS_VACCINATED_1PLUS_DOSE'])
    # Calculates total pop of country from given info(per 100 vaccinated and # people vaccinated)
    data_most_tourism['Total Population'] = \
        (data_most_tourism['PERSONS_VACCINATED_1PLUS_DOSE'] / (
                data_most_tourism['PERSONS_VACCINATED_1PLUS_DOSE_PER100'] / 100))
    # Calculates total population not at all vaccinated
    data_most_tourism['NoVax'] = (
            data_most_tourism['Total Population'] - data_most_tourism['PERSONS_VACCINATED_1PLUS_DOSE'])
    # sorts the data by population
    data_most_tourism = data_most_tourism.sort_values(by=['Total Population'], ascending=False)

    # --- Preparing data and layout ---
    # 3 trace's used for each stacking level of the bar chart
    trace1 = go.Bar(x=data_most_tourism['COUNTRY'], y=data_most_tourism['NoVax'], name='No Vax')
    trace2 = go.Bar(x=data_most_tourism['COUNTRY'],
                    y=(data_most_tourism['PERSONS_VACCINATED_1PLUS_DOSE'] - data_most_tourism['FullVax']),
                    name='Partial Vax')
    trace3 = go.Bar(x=data_most_tourism['COUNTRY'], y=data_most_tourism['FullVax'], name='Full Vax')
    # sets data for graph
    graph_most_tourism = [trace1, trace2, trace3]
    # sets layout for graph
    lay = go.Layout(title='Title Here',
                    xaxis={'title': 'Country'},
                    yaxis={'title': 'Population'}, barmode='stack')

    # --- Plot the figure and return it ---
    fig = go.Figure(data=graph_most_tourism, layout=lay)
    return fig


# --------------------------------
# CHOROPLETH MAP United States Vaccination Distribution
# --------------------------------
def choropleth1_USA():
    # --- Filtering data ---
    data_vax_usa = data_vax_usaDist
    # changes the data type of time values in dataframe
    data_vax_usa['Week of Allocations'] = pd.to_datetime(data_vax_usa['Week of Allocations'])
    # sorts out all old data
    data_vax_usa = data_vax_usa.sort_values(by=['Week of Allocations'], ascending=[False]).head(60)
    data_vax_usa = data_vax_usa.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Removing empty spaces
    data_vax_usa['Jurisdiction'] = data_vax_usa['Jurisdiction'].apply(lambda x: state_codes[x])  # Replaces State Names

    # --- Plot the figure and return it ---
    fig = px.choropleth(data_vax_usa, locations='Jurisdiction', locationmode='USA-states',
                        color="1st Dose Allocations",
                        hover_name='Jurisdiction', projection="albers usa", title="Vaccine allocation by state",
                        color_continuous_scale=px.colors.sequential.Agsunset)
    return fig

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]  # css stylesheet
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

# data used to create graph
data_usa_cases = pd.read_csv('../Datasets/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

# State codes dictionary used for translation
state_codes = {
    'District of Columbia': 'DC', 'Mississippi': 'MS', 'Oklahoma': 'OK',
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
    'Nevada': 'NV', 'Maine': 'ME'}

states = list(state_codes.values())  # creates list from dict
states.sort()  # Sorts the values of states
line_data = data_usa_cases  # creates date frame
line_data['submission_date'] = pd.to_datetime(line_data['submission_date'])  # changes data type of date value
line_data = line_data[line_data['state'] == 'FL']  # sets default line data
line_data = line_data.sort_values(by=['submission_date'], ascending=[False]).head(30)  # sorts data by date
# plots line for final chart
line_datachart = [go.Scatter(x=line_data['submission_date'], y=line_data['new_case'], mode='lines', name='Death')]

# sets app layout
app.layout = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H5("Select a State"),
            # dropdown used to select state for interactive line chart
            dcc.Dropdown(
                id='select-country',
                options=[
                    {'label': state, 'value': state} for state in states
                ],
                value=list(state_codes.values())[0]
            ),
        ], width=2, align="center", style={"padding-bottom": "3rem"}),
        dbc.Col(children=[
            dcc.Graph(id='graph1'),
        ]),
    ], style={"padding-bottom": "3rem"}),
    dbc.Row(children=[
        html.P(
            "The Centers for Disease Control and Prevention said on Saturday about 146.2 million people have"
            " received at least one dose of a Covid-19 vaccine, including about 103.4 million people who have been"
            " fully vaccinated by Johnson & Johnson’s single-dose vaccine or the two-dose series made by "
            "Pfizer-BioNTech and Moderna.\n"
            "Providers are administering about 2.55 million doses per day on average, about a 25 percent decrease"
            "from the peak of 3.38 million reported on April 13.)")
    ])
], className="container-xl", )


# called by callback and used to update graph on page with new states
def update_figure(select_state):
    nline_data = data_usa_cases
    nline_data['submission_date'] = pd.to_datetime(nline_data['submission_date'])
    nline_data = nline_data[nline_data['state'] == select_state]
    nline_data = nline_data.sort_values(by=['submission_date'], ascending=[False]).head(30)

    new_line_data = [go.Scatter(x=nline_data['submission_date'], y=nline_data['new_case'], mode='lines', name='Death')]

    # returns the new data frame for graph
    return {'data': new_line_data,
            'layout': go.Layout(title='Corona Virus Confirmed Cases in ' + select_state,
                                xaxis={'title': 'Country'},
                                yaxis={'title': 'Number of confirmed cases'})}


# returns the layout of full page
def getLayout():
    return app.layout


if __name__ == "__main__":
    app.run_server()

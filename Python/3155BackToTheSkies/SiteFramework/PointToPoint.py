import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import Header as header

external_stylesheets = ["../assets/bootstrap.min.css"]
app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

data_usa_cases = pd.read_csv('../Datasets/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

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

states = list(state_codes.values())
line_data = data_usa_cases
line_data['submission_date'] = pd.to_datetime(line_data['submission_date'])
line_data = line_data[line_data['state'] == 'FL']
line_data = line_data.sort_values(by=['submission_date'], ascending=[False]).head(30)
line_datachart = [go.Scatter(x=line_data['submission_date'], y=line_data['new_case'], mode='lines', name='Death')]

app.layout = html.Div(children=[
    header.getHeader(),
    dbc.Row(children=[
        dbc.Col(children=[
            html.P(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                "labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra "
                "maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."),
            dcc.Dropdown(
                id='select-country',
                options=[
                    {'label': state, 'value': state} for state in state_codes.values()
                ],
                value=list(state_codes.values())[0]
            ),
        ], style={"width": "1"}),
        dbc.Col(children=[
            dcc.Graph(id='graph1'),
        ], style={"background-color": "#000000", }),
    ])
], className="container-xl", )


# @app.callback(Output('graph1', 'figure'),
#               [Input('select-country', 'value')])
def update_figure(select_state):
    nline_data = data_usa_cases
    nline_data['submission_date'] = pd.to_datetime(nline_data['submission_date'])
    nline_data = nline_data[nline_data['state'] == select_state]
    nline_data = nline_data.sort_values(by=['submission_date'], ascending=[False]).head(30)

    new_line_data = [go.Scatter(x=nline_data['submission_date'], y=nline_data['new_case'], mode='lines', name='Death')]

    return {'data': new_line_data,
            'layout': go.Layout(title='Corona Virus Confirmed Cases in ' + select_state,
                                xaxis={'title': 'Country'},
                                yaxis={'title': 'Number of confirmed cases'})}


def getLayout():
    return app.layout


if __name__ == "__main__":
    app.run_server()

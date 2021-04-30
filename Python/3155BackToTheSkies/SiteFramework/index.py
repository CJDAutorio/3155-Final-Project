import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import Home as home
import SeeTheData as seeTheData
import DataView as dataView

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.getLayout()
    elif pathname == '/see_the_data':
        return seeTheData.getLayout()
    elif pathname == '/see_the_data':
        return seeTheData.getLayout()
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

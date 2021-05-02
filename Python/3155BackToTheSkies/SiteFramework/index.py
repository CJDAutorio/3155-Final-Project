import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import Home as home
import SeeTheData as seeTheData
import DataView as dataView
import ChartsMega as chm
import PointToPoint as p2p
import AboutUs as aboutUs
import SeeTheProcedures as aboutCovid

# displays every page on the site
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# runs a callback each time the url changes to bring up the new page
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.getLayout()
    elif pathname == '/see_the_data':
        return seeTheData.getLayout()
    elif pathname == '/about_us':

        return aboutUs.getLayout()
    elif pathname == '/data_view1':
        return dataView.getLayout1()
    elif pathname == '/data_view2':
        return dataView.getLayout2()
    elif pathname == '/data_view3':
        return dataView.getLayout3()
    elif pathname == '/data_view4':
        return dataView.getLayout4()
    elif pathname == '/data_view5':
        return dataView.getLayout5()
    elif pathname == '/data_view6':
        return aboutCovid.getLayout()
    elif pathname == '/p2p':
        return p2p.getLayout()

# runs a callback each time the state is changes on the p2p page
@app.callback(Output('graph1', 'figure'),
              [Input('select-country', 'value')])
def update_figure(select_state):
    return p2p.update_figure(select_state)


if __name__ == '__main__':
    app.run_server(debug=True)

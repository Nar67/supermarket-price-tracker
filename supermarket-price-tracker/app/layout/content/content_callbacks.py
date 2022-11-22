from dash.dependencies import Input, Output, State
from app import app

from dash import html
import dash_bootstrap_components as dbc
from dash import dcc


home_content = dcc.Markdown(
    '''
    # Welcome to the Supermarket Price Tracker!
    '''
, style={'margin-top': '30px'})

@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return home_content
#    elif pathname == "/table":
#        return data_table
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

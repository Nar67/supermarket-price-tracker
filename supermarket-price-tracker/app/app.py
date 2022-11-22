import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from layout.layout import layout
from maindash import app
from layout.sidebar.sidebar_callbacks import *
from layout.content.content_callbacks import *

app.layout = layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8889, debug=True)

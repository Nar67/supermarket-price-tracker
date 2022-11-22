from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from layout.sidebar.sidebar_styles import SIDEBAR_STYLE

sidebar = html.Div(
    [
        html.H2("Menu"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", id="home-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

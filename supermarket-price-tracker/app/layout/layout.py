     
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


from layout.sidebar.sidebar import sidebar
from layout.content.content import content


navbar = dbc.NavbarSimple(
    children=[],
    id="navBar",
    brand="Supermarket Price Tracker",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
)

layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)
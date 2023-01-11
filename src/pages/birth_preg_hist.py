import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/birth_preg_hist',  # '/' is home page and it represents the url
                   name='Birth Pregnancy Histories',  # name of page, commonly used as name of link
                   title='Birth Pregnancy Histories',  # title that appears on browser's tab
)

layout = html.Div(
    [
        dcc.Markdown('# Add Contents')
    ]
)
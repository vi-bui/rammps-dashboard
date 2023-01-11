import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/sibling_survival_hist',  # '/' is home page and it represents the url
                   name='Sibling Survival Histories',  # name of page, commonly used as name of link
                   title='Sibling Survival Histories',  # title that appears on browser's tab
)

layout = html.Div(
    [
        dcc.Markdown('# Add Contents')
    ]
)
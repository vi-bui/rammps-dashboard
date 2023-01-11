import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

dash.register_page(__name__,
                   path='/responserates',  # represents the url text
                   name='Response Rates',  # name of page, commonly used as name of link
                   title='Responses'  # represents the title of browser's tab
)

# page 2 data

# read in data
df = pd.read_csv("src/data/calls.csv")
df = df[df['group'].isin(['DRC', 'MW', 'BF-RDD'])] # select specific countries

layout = html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/smoking2.jpg')
                ], width=4
            ),
            dbc.Col(
                [
                    dcc.Dropdown(df.group.unique(), id='country', value='DRC')
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig',
                              figure=px.bar(df, x='Outcome2', y='percperoutcome'))
                ], width=12
            )
        ])
    ]
)


@callback(
    Output('bar-fig', 'figure'),
    Input('country', 'value')
)
def update_graph(value):
    dff = df[df.group==value]
    fig = px.bar(dff, x='Outcome2', y='percperoutcome', color = 'Eligibility',
    labels={'Outcome2' : '', 'percperoutcome' : 'Phonec calls'})
    fig.update_yaxes(range = [0,80]) # set range for yaxis
    fig.update_layout( yaxis={'categoryorder':'trace', 'categoryarray':df.index})
    return fig
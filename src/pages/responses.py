import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__,
                   path='/responserates',  # represents the url text
                   name='Response Rates',  # name of page, commonly used as name of link
                   title='Responses'  # represents the title of browser's tab
)

# page 2 data
df = pd.read_csv("src/data/calls.csv")

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
                    dcc.RadioItems(df.group.unique(), id='country', value='DRC')
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
    fig = px.bar(dff, x='Outcome2', y='percperoutcome')
    return fig
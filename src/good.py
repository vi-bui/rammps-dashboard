import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from PIL import Image

dash.register_page(__name__,
                   path='/responserates',  # represents the url text
                   name='Response Rates',  # name of page, commonly used as name of link
                   title='Responses'  # represents the title of browser's tab
)

# page 2 data

# read in data
df = pd.read_csv("src/data/calls.csv")
df = df[df['group'].isin(['DRC', 'MW', 'BF-RDD'])] # select specific countries


# plots_fig = 'assets/plot.png'
# age_sex_bf_plot = 'assets/age_sex_bf_plot.png'
# fig_names = ['plots_fig', 'age_sex_bf_plot']
fig_names = ['src/assets/plot.png', 'src/assets/age_sex_bf_plot.png']
print(fig_names[0])

layout = html.Div(
    [
        dbc.Row([

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
        ]),
        dbc.Row([
             dbc.Col(
                [
                    dcc.Dropdown(
                        id='fig_dropdown',
                        options=[{'label': x, 'value': x} for x in fig_names],
                        value=None
                    )
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                html.Div(
                    children=[
                    html.Div(id='fig_plot'),
        ]
    )  
                ], width=12
            )
        ])
    ]
)


@callback(
    [Output('bar-fig', 'figure'),Output('fig_plot', 'children')],
    [Input('country', 'value'), Input('fig_dropdown', 'value')]
)

# @callback(
#     Output('bar-fig', 'figure'),
#     Input('country', 'value')
# )

def update_graph(value, static_plot):
    
    if static_plot == "src/assets/plot.png":
        img = Image.open(fig_names[0])
        static_fig = px.imshow(img, binary_format='png', width=1000, height=1000)
        static_fig.update_xaxes(showticklabels=False)
        static_fig.update_yaxes(showticklabels=False)


        dff = df[df.group==value]
        fig = px.bar(dff, x='Outcome2', y='percperoutcome', color = 'Eligibility', category_orders={'Outcome2': df.index[::-1]},
        labels={'Outcome2' : '', 'percperoutcome' : 'Phonec calls'})
        fig.update_yaxes(range = [0,80]) # set range for yaxis

        return fig, dcc.Graph(figure=static_fig, style={'width': '10vh', 'height': '10vh'})
    
    else:
        img = Image.open(fig_names[1])
        static_fig = px.imshow(img, binary_format='png')
        static_fig.update_xaxes(showticklabels=False)
        static_fig.update_yaxes(showticklabels=False)

        dff = df[df.group==value]
        fig = px.bar(dff, x='Outcome2', y='percperoutcome', color = 'Eligibility', category_orders={'Outcome2': df.index[::-1]},
        labels={'Outcome2' : '', 'percperoutcome' : 'Phonec calls'})
        fig.update_yaxes(range = [0,80]) # set range for yaxis

        return fig, dcc.Graph(figure=static_fig, style={'width': '90vh', 'height': '90vh'})


# def update_output(value):
#     if value == "plot_fig":
#         img = Image.open(fig_names[0])
#         fig = px.imshow(np.array(img))
#         return fig.show()
#     else:
#         img = Image.open(fig_names[1])
#         fig = px.imshow(np.array(img))
#         return fig.show()



# https://stackoverflow.com/questions/62175996/plotly-dash-dropdown-menu-python
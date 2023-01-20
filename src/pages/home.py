import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import subprocess
from PIL import Image

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='Home',  # title that appears on browser's tab
)

data = {
  "Country": ['Malawi', 'The Democratic Republic of Congo', 'Burkina Faso'],
  "iso_alpha": ['MWI', 'COD', 'BFA'],
  "catis_completed":[6796, 11952, 8729]
}
#load data into a DataFrame object:
world_catis = pd.DataFrame(data)


process2 = subprocess.Popen(["Rscript", "src/testscript.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(process2)
result2 = process2.communicate()
print(result2)
image_path = Image.open('assets/plot.png')

# page 1 data
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                    dcc.Graph(id='map-fig',
                        figure = px.scatter_geo(world_catis, locations="iso_alpha", color="Country",
                        hover_name="Country", size="catis_completed",
                        projection="natural earth"))
                    ], width=12
                ),
                dbc.Col(
                    [
                    html.Img(src='assets/plot.png', style={'height':'80%', 'width':'80%'})
                    ], width=13
                )

            ]
        )
    ]
)

## https://appsilon.com/use-r-and-python-together/#call-r-scripts
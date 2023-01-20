import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image

# df = pd.read_csv("src/data/calls.csv")
# df[df['group'].isin(['DRC', 'MW', 'BF-RDD'])]
# print(df)

# #fig = px.bar(df, x='Outcome2', y='percperoutcome')
# #fig.show()

# dff = px.data.tips()
# print(dff)

# ### create world map
# import pandas as pd 

# data = {
#   "country": ['Malawi', 'The Democratic Republic of Congo', 'Burkina Faso'],
#   "iso_alpha": ['MWI', 'COD', 'BFA'],
#   "catis_comp":[6796, 11952, 8729]
# }

# #load data into a DataFrame object:
# world_catis = pd.DataFrame(data)

# print(world_catis) 

# fig = px.scatter_geo(world_catis, locations="iso_alpha", color="country",
#                      hover_name="country", size="catis_completed",
#                      projection="natural earth")
# fig.show()

plot = 'assets/plot.png'
print(plot)
fig_names = ['src/assets/plot.png', 'src/assets/age_sex_bf_plot.png']
img = Image.open(fig_names[0])
# fig = px.imshow(np.array(img))
fig = px.imshow(img, color_continuous_scale='gray')
fig.update_layout(coloraxis_showscale=False)
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)
fig.show()
# fig.show()



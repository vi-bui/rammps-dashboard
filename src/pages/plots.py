import pandas as pd
import plotly.express as px
import numpy as np


df = pd.read_csv("src/data/calls.csv")
df[df['group'].isin(['DRC', 'MW', 'BF-RDD'])]
print(df)

#fig = px.bar(df, x='Outcome2', y='percperoutcome')
#fig.show()

dff = px.data.tips()
print(dff)


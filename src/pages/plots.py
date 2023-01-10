import pandas as pd
import plotly.express as px


df = pd.read_csv("src/data/calls.csv")
print(df)
#fig = px.bar(df, x='Outcome2', y='percperoutcome')
#fig.show()

dff = px.data.tips()
print(dff)
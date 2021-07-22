import plotly.express as px
import pandas as pd

from config.settings import DATA_DIRS

df_il2 = pd.read_csv(DATA_DIRS[0]+'/literacy_all.csv')
df_mp2 = pd.read_csv(DATA_DIRS[0]+'/happiness_pwrindx.csv')
print(df_mp2)
print(df_il2)
fig = px.scatter(df_mp2, x="mililtarypower", y="score", color="region", hover_data=['country'])
fig.show()
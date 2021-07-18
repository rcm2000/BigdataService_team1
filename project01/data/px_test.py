import plotly.express as px
import pandas as pd
df = pd.read_csv('C:\BigdataProjects\BigdataService_team1\project01\data\data02.csv')
fig = px.choropleth(df, locations='country', locationmode='country names',
                    color='score',
                    animation_frame = 'year',
                    basemap_visible=False,
                    color_continuous_scale='Purpor_r',
                    title=('Happiness score 2015-2021 Report')
                   )
fig.update_layout(height=600)
fig.show()
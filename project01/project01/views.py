from django.shortcuts import render
from matplotlib import pyplot as plt
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns

from config.settings import DATA_DIRS

df = pd.read_csv(DATA_DIRS[0]+'/data03.csv')
df_exp = pd.read_csv(DATA_DIRS[0]+'/data_express.csv')
df11 = pd.read_csv(DATA_DIRS[0]+'/country11.csv')

# Create your views here.
def home(request):

	return render(request, 'index.html')
def index(request):
	fig = plot(px.choropleth(df, locations='country', locationmode='country names',
						color='score',
						animation_frame='year',
						basemap_visible=True,
						color_continuous_scale='Tropic'
						),output_type='div')

	return render(request, 'index.html', context={'plot_div': fig})
def dashboard(request):

	return render(request, 'dashboard.html')
def information(request):

	return render(request, 'information.html')
def info(request):

	return render(request, 'info.html')
def test(request):
	fig1 = plot(px.histogram(df, x='score', nbins=20, animation_frame='year'),output_type='div')




	return render(request, "test.html", context={})

def table(request):

	return render(request, 'table.html')
def datatable(request):

	return render(request, 'datatable.html')
def chart(request):

	return render(request, 'chart.html')
def authlogin(request):

	return render(request, 'authlogin.html')
def authregister(request):

	return render(request, 'authregister.html')
def authforgotpassword(request):

	return render(request, 'authforgotpassword.html')
def summary(request):

	return render(request, 'summary.html')
def social(request):
	fig4 = plot(px.histogram(df, x='social_support_std', nbins=20, animation_frame='year',
                    title='Social support histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="social_support_std", animation_frame='year', color='region',
				  title='Regional social support boxplot', facet_col='region')
	fig3.update_layout(yaxis_range=[-3.2, 2])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df01 = df11[['year', 'country', 'social_support_std']]
	fig1 = plot(
		px.bar(df01, x="social_support_std", y="country", animation_frame="year", color="country", orientation="h",
                    		title='Country11'),output_type='div')
	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							 color='social_support_std',
							 animation_frame='year',
							 basemap_visible=True,
							 color_continuous_scale='Tropic',
                    		title=('World social support map')
							 ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="socialsupport", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title=('Regional social support scatter plot')), output_type='div')
	sss = pd.DataFrame(df_exp['socialsupport'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="socialsupport", animation_frame="year", color="region", barmode="group",
                    		title=('Regional social support bar plot')),
			   output_type='div')
	return render(request, 'social.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def health(request):
	fig4 = plot(px.histogram(df, x='health_std', nbins=20, animation_frame='year',title='Health histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="health_std", animation_frame='year', color='region',
					   title='Regional health boxplot', facet_col='region', )
	fig3.update_layout(yaxis_range=[-3.2, 2])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df02 = df11[['year', 'country', 'health_std']]
	fig1 = plot(px.bar(df02, x="health_std", y="country", animation_frame="year", color="country", orientation="h",
                    		title='Country11'),
				output_type='div')
	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							  color='health_std',
							  animation_frame='year',
							  basemap_visible=True,
							  color_continuous_scale='Tropic',
                    		title='World health map'
							  ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="health", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title='Regional health scatter plot'), output_type='div')
	sss = pd.DataFrame(df_exp['health'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="health", animation_frame="year", color="region", barmode="group",
                    		title=('Regional health bar plot')),
			   output_type='div')
	return render(request, 'health.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def gdp(request):
	fig4 = plot(px.histogram(df, x='gdp_std', nbins=20, animation_frame='year',title='Gdp histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="gdp_std", animation_frame='year', color='region', title='Regional gdp boxplot',
			   facet_col='region')
	fig3.update_layout(yaxis_range=[-3, 3.3])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df03 = df11[['year', 'country', 'gdp_std']]
	fig1 = plot(px.bar(df03, x="gdp_std", y="country", animation_frame="year", color="country",title='Country11', orientation="h"),
				output_type='div')

	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							  color='gdp_std',
							  animation_frame='year',
							  basemap_visible=True,
							  color_continuous_scale='Tropic',
                    		title='World Gdp map'
							  ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="gdp", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title='Regional Gdp scatter plot'), output_type='div')
	sss = pd.DataFrame(df_exp['gdp'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="gdp", animation_frame="year", color="region", barmode="group",
                    		title=('Regional gdp bar plot')),
			   output_type='div')
	return render(request, 'gdp.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def etc(request):
	plot_div1 = plot(
		px.scatter(df_exp, x="freedom", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div2 = plot(
		px.scatter(df_exp, x="trust", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div3 = plot(
		px.scatter(df_exp, x="generosity", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	return render(request, 'etc.html',context={'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_div3': plot_div3,})
def info2(request):

	return render(request, 'info2.html')
def covid19(request):

	return render(request, 'covid19.html')
def militarypower(request):

	return render(request, 'militarypower.html')
def illiteracyrate(request):

	return render(request, 'illiteracyrate.html')
def summary2(request):

	return render(request, 'summary2.html')
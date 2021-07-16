from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly
import plotly.express as px
import pandas as pd

# Create your views here.
def home(request):

	return render(request, 'index.html')
def index(request):

	return render(request, 'index.html')
def dashboard(request):

	return render(request, 'dashboard.html')
def information(request):

	return render(request, 'information.html')
def info(request):

	return render(request, 'info.html')
def test(request):
	df = pd.read_csv('C:\BigdataProjects\BigdataService_team1\project01\data\data_sorted.csv')
	plot_div1 = plot(px.scatter(df, x="gdp_std", y="score", animation_frame="year", animation_group="country", color="region", hover_name="country", facet_col="region",
           log_x=False, size_max=45, range_x=[-3,3], range_y=[0,10]),output_type='div')
	plot_div2 = plot(
		px.scatter(df, x="health_std", y="score", animation_frame="year", animation_group="country", color="region",
				   hover_name="country", facet_col="region",
				   log_x=False, size_max=45, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div3 = plot(
		px.scatter(df, x="freedom_std", y="score", animation_frame="year", animation_group="country", color="region",
				   hover_name="country", facet_col="region",
				   log_x=False, size_max=45, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div4 = plot(
		px.scatter(df, x="trust_std", y="score", animation_frame="year", animation_group="country", color="region",
				   hover_name="country", facet_col="region",
				   log_x=False, size_max=45, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div5 = plot(
		px.scatter(df, x="generosity_std", y="score", animation_frame="year", animation_group="country", color="region",
				   hover_name="country", facet_col="region",
				   log_x=False, size_max=45, range_x=[-3, 3], range_y=[0, 10]), output_type='div')

	sss = pd.DataFrame(df['social_support_std'].groupby([df['year'], df['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="social_support_std", animation_frame="year", color="region", barmode="group"), output_type='div')

	return render(request, "test.html", context={'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_div3': plot_div3,'plot_div4': plot_div4,'plot_div5': plot_div5,'plot_div6': fig,})

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
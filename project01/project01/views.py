from django.shortcuts import render

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

	return render(request, 'test.html')
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
from django.shortcuts import render

def index_page(request):
	return render(request, 'layout_app/index.html')

def main_page(request):
	return render(request, 'layout_app/main_page.html')

def about_page(request):
	return render(request, 'layout_app/about_page.html')

def help_page(request):
	return render(request, 'layout_app/help.html')
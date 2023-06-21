from django.urls import path
from .views import *

urlpatterns = [
	path('', cats_page, name='cats_page'),
	path('<str:cats_name>', cat, name='cat')
]

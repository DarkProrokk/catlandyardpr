from django.contrib import admin
from django.urls import path
from layout_app.views import *
from cats_page.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats/', include('cats_page.urls')),
    path('', main_page, name='main_page'),
    path('about', about_page, name='about_page'),
    path('help', help_page, name='help_page'),
    path('<cat>', cat),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
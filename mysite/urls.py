from myapp import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls')),
    path('personal/<some_name>', include('myapp.urls')),
    path('random', include('myapp.urls')),
    path('admin/', admin.site.urls),
]

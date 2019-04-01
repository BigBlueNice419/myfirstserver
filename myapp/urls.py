from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personal/<some_name>', views.personal, name="personal"),
    path('random', views.random, name='random'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test1', views.test1, name='test1'),
]

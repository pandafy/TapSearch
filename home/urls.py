from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home-home'),
    path('add',views.add,name='home-add'),
    path('clear',views.clear,name='home-clear')
]
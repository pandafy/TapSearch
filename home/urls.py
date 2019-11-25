from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListsDocumentView.as_view(),name="home"),
    path('search',views.SearchDocumentView.as_view(),name="search"),
       
    path('clear',views.clear,name='clear')
]
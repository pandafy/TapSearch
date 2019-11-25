from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListsDocumentView.as_view(),name="api-home"),
    path('search',views.SearchDocumentView.as_view(),name="api-search"),   
    path('clear',views.clear,name='api-clear')
]
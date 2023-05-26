from django.urls import path
from . import views

app_name = 'serach_app'

urlpatterns = [
    path('',views.searchResult, name='search')
]
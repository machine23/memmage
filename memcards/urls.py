from django.urls import path
from . import views


app_name = 'memcards'
urlpatterns = [
    path('', views.index, name='index'),
]

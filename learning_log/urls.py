from .views import *
from django.urls import path

urlpatterns = [
    path('', home_page),
    path('main/', main_page),
    path('news/<int:newsid>/', news_page),
]

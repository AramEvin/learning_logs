from . import views
from django.urls import path


app_name = 'learning_log'
urlpatterns = [
    path('', views.home_page, name='Home'),
    path('main/', views.main_page, name='Main'),
    path('news/<int:newsid>/', views.news_page, name='News'),
]

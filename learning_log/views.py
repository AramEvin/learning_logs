from django.shortcuts import render
from django.http import HttpResponse
from .models import New_title

def home_page(request):
    return render(request, 'learning_log/home_page.html')

def main_page(request):
    return render(request, 'learning_log/main_page.html')

def news_page(request, newsid):
    if newsid == 0:
        return HttpResponse("<p><h1>Sorry page not fonud<h1></p>")
    elif newsid <= 100:
        return render(request, 'learning_log/news_page.html')
    else:
        return HttpResponse("<p><h1>Sorry page not fonud<h1></p>")





from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('Home Page!')

def main_page(request):
    return HttpResponse('Hello in Main page !')

def news_page(request, newsid):
    if newsid <= 100:
        return HttpResponse(f'Hello in News : {newsid} page')
    else:
        return HttpResponse(f'Sorry we dosnt have page : {newsid}')



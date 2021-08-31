from django.http import response
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup

# Create your views here.

def home(req):
    
    return render(req, 'home.html')

def getPrice(req, cripto):

    
    print('>>>>>>>>>>>>>>>>>>>>>', cripto)
    url = 'https://markets.businessinsider.com/currencies/'+cripto+'-usd'
    html =  requests.get(url)

    bs = BeautifulSoup(html.content, 'html.parser')
    
    price = bs.find('span', {'class': 'price-section__current-value'})
    #coin = bs.findAll('h2', {'clas': 'sc-1q9q90x-0 jCInrl h1'})
    price = price.text
    print('price-----------------------', price)

    response = {
        'price': price,
        'coin': cripto,
    }

    return JsonResponse(response)
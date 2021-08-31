from django.http import response
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, JsonResponse, Http404
from bs4 import BeautifulSoup
import re


# Create your views here.

def home(req):
    
    return render(req, 'home.html')


def getPrice(req, cripto):

    
    print('>>>>>>>>>>>>>>>>>>>>>', cripto)
    try:
        url = 'https://markets.businessinsider.com/currencies/'+cripto+'-usd'
        html =  requests.get(url)

        bs = BeautifulSoup(html.content, 'html.parser')
        
        price = bs.find('span', {'class': 'price-section__current-value'})
        #coin = bs.findAll('h2', {'clas': 'sc-1q9q90x-0 jCInrl h1'})
        price = price.text
        print('price-----------------------', price)

    except Exception as e:
        raise Http404("Cannot get price of "+cripto)


    response = {
        'price': price,
        'cur': 'usd'
    }

    return JsonResponse(response)

def getAllinfo(req, cripto):
    
    
    print('>>>>>>>>>>>>>>>>>>>>>', cripto)
    response = {}
    try:
        url = 'https://markets.businessinsider.com/currencies/'+cripto+'-usd'
        html =  requests.get(url)

        bs = BeautifulSoup(html.content, 'html.parser')
        
        price = bs.find('span', {'class': 'price-section__current-value'})
        #coin = bs.findAll('h2', {'clas': 'sc-1q9q90x-0 jCInrl h1'})
        price = price.text
        #print('price-----------------------', price)
        response['price'] = price
        response['cur'] = 'usd'
        snapshot = bs.find('div', {'class': 'snapshot'})
        data_items = snapshot.findAll('div', {'class': 'snapshot__data-item'})
        for data in data_items:
            data = data.text.split('\n')[1::]

            for i in range(len(data)):
                data[i] = re.sub('[\t*\r]', '', data[i])
                
            data = data[0:-1]
            #print(data)
            #print('-------------')
            response[data[1]] = data[0]
        
    
    except Exception as e:
        raise Http404("Cannot get price of "+cripto)



    return JsonResponse(response)
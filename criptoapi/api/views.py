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
        url = 'https://www.cointracker.io/price/'+cripto
        html =  requests.get(url)

        bs = BeautifulSoup(html.content, 'html.parser')

        price = bs.find('div', {'class': 'my-auto h4'}).text
        price = re.sub('\n', '', price)
        response = {
        'price': price,
        'cur': 'usd'
        }

    except Exception as e:
        raise Http404("Cannot get price of "+cripto)

    return JsonResponse(response)



def getAllinfo(req, cripto):
    
    print('>>>>>>>>>>>>>>>>>>>>>', cripto)
    response = {}

    try:
        
        url = 'https://www.cointracker.io/price/'+cripto
        html =  requests.get(url)

        bs = BeautifulSoup(html.content, 'html.parser')
        
        infos = bs.findAll('div', {'class': 'my-auto h4'})
        print(infos)
        for idx, info in enumerate(infos):
            infos[idx] = re.sub('\n', '', info.text)

        try:
            about = bs.find('p', {'class': 'card-text'})
            about = about.text
        except:
            about = 'empty'

        response = {
            'price': infos[0],
            'marketcap': infos[1],
            '24h volume': infos[2],
            'about_coin': about
        }

    except Exception as e:
        print(e)
        raise Http404("Cannot get price of "+cripto)



    return JsonResponse(response)
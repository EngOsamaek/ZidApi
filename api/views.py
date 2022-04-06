from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests import request as req
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
#api endpoint for sending order data (api/sendOrderData)


@csrf_exempt
@api_view(['GET'])
def callback(request):
    url = "https://oauth.zid.sa/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": "567",
        "client_secret": "Gbjh5eEuWQ1isKYxsLpmBqcY1LReps0JYu04Iiij",
        "redirect_uri": "https://zidapi.rozahsoft.com/oauth/callback",
        "code": request.GET.get('code'),
    }
    response = req("POST", url, data=data)
    print(response.json)
    return  redirect('https://web.zid.sa/market/my-apps')


@csrf_exempt
@api_view(['GET'])
def red(request):
    return  redirect('https://oauth.zid.sa/oauth/authorize?client_id=567&redirect_uri=https%3A%2F%2Fzidapi.rozahsoft.com%2Foauth%2Fcallback&response_type=code')
    
    
    
    
    
@csrf_exempt
@api_view(['GET'])
def apitest(request): 
    url = "https://oauth.zid.sa/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": request.GET.get('client_id'),
        "client_secret": request.GET.get('client_secret'),
        "redirect_uri": "https://zidapi.rozahsoft.com/oauth/callback",
        "code": request.GET.get('code'),
    }
    response = req("POST", url, data=data)
    
    #print(response.json)
    return HttpResponse(response, content_type='application/json')
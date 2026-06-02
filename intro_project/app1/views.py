from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def great(request):
    return HttpResponse('hi this is ur greeting')
def getname(request):
    return HttpResponse('hi this is soemthing')
def users(request):
    data=[
        {'name':'revanth',
         'age':20,
         },
        {'name':'john',
         'age':30,
         },
        {'name':'lucy',
         'age':40,}
    ]
    return JsonResponse(data, safe=False)
def greet_to_users(request,name):
    return HttpResponse(f"hi {name} , this is ur greeting")
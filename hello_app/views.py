from django.http import JsonResponse
from django.shortcuts import render

def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_world_html(request):
    return render(request, 'hello.html')

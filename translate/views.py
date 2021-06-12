from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def index(request):
    return render(request,'index.html')
def fetching(request):
    if request.method=='GET':
        lang=request.GET['lang']
        text=request.GET['text']

        print()
        mytex=text.strip().split(" ")
        text=mytex[len(mytex)-1]
        responce=requests.get("https://xlit.quillpad.in/quillpad_backend2/processWordJSON?lang="+lang+"&inString="+text)
        data=responce.json()
        return JsonResponse(data)
    print("lol")
    data_responce={}
    data_responce['status']='ok'
    data_responce['code']=500
    return JsonResponse(data_responce)

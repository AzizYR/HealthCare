from django.shortcuts import render , render_to_response
from django.http import HttpResponse
import requests
from . models import events
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import pythoncom
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def index(request):

    sympapiurl = 'https://healthservice.priaid.ch/symptoms?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJvdXJuZWphc29tQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMjE4NyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjEwOCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiIxMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJCYXNpYyIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTktMDMtMzAiLCJpc3MiOiJodHRwczovL2F1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1NTQwMDMxOTUsIm5iZiI6MTU1Mzk5NTk5NX0.6jfHY8Svx35hiBY3ZgKbTxmOzfY6cbmMWu3GSFV9iUo&format=json&language=en-gb'
    r = requests.get(sympapiurl).json()
    dataset = events.objects.all()
    data = dataset.get(name = 'Harsh')

    return render(request , 'dashboard/index.html' ,{'r' : r , 'data':data })


def charts(request):
    
    return render(request, 'dashboard/charts.html')

def push(request):
    return render(request, 'dashboard/push.html')


def chatbot(request):
    requestlist = []
    responselist = []
    pythoncom.CoInitialize()
    dataset = events.objects.all()
    data = dataset.get(name = 'Harsh')
    bot = ChatBot('Sheku',tie_breaking_method="random_response")
    trainer = ListTrainer(bot)
    sheku = pyttsx3.init()

    for _file in os.listdir('files'):
    	chats = open("files/" + _file , 'r').readlines()


    trainer.train(chats)

    request = request.POST['message']
    requestlist.append(request)
    response = bot.get_response(request)
    responselist.append(response)
    sheku.say(response)
    print(response)
    sheku.runAndWait()
    analyzer = SentimentIntensityAnalyzer()
    analy = analyzer.polarity_scores(response)

    if(analy['neg'] == 0.9 ):
        print("Sending a Text!")
        url = "https://www.fast2sms.com/dev/bulk"

        querystring = {"authorization":"oA10WXBMQbDtzSvRa5g3yhYl9kqEdNJZjscIrUfPxOu82w7GeTszBb1Yy5q7nTvjOg8fSolx0wuci2IX","sender_id":"FSTSMS","message":"Emergency Message! I am In Distress, Please reach out to me!","language":"english","route":"t","numbers":"8898427027,9930335323,7021272227,7718904478"}

        headers = {
            'cache-control': "no-cache"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)


    return render_to_response('dashboard/widgets.html' , { 'requestlist': requestlist , 'responselist': responselist })


def widgets(request):
    # pythoncom.CoInitialize()
    dataset = events.objects.all()
    data = dataset.get(name = 'Harsh')
    # bot = ChatBot('Sheku',tie_breaking_method="random_response")
    # trainer = ListTrainer(bot)
    # sheku = pyttsx3.init()
    #
    # for _file in os.listdir('files'):
    # 	chats = open("files/" + _file , 'r').readlines()
    #
    # trainer.train(chats)
    #
    # request = request.POST['message']
    # response = bot.get_response(request)
    # sheku.say(response)
    # print(response)
    # sheku.runAndWait()
    #

    # while True:
    # 	request = input(data.name +':')
    # 	response = bot.get_response(request)
    # 	sheku.say(response)
    # 	print("Sheku:",response)
    # 	sheku.runAndWait()


    return render(request, 'dashboard/widgets.html' , { 'data': data})

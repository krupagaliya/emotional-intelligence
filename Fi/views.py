from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import urllib
import urllib.request
import urllib.parse
from Fi.kk import sen,sa,so
import json


def index(request):
    return render(request, "Fi/home.html",{})

def instantResult(request):
    if (request.method == "POST"):
        mood_ans = request.POST['mood_ans']
        busy_ans = request.POST['busy_ans']
        sleep_ans = request.POST['sleep_ans']
        belive_ans = request.POST['belive_ans']
        #opinion_ans = request.POST['opinion_ans']  opinion_ans\\

        tmp = urllib.parse.urlencode({"text": mood_ans +" "+ busy_ans +" "+ sleep_ans +" "+ belive_ans+" "}).encode("utf-8")
        res = urllib.request.urlopen("http://text-processing.com/api/sentiment/", tmp).read()
        dstr = res.decode()

        json_acceptable_string = dstr.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        print(type(res))
        nut = d['probability']["neutral"]*100
        pos = d['probability']["pos"]*100
        neg= d['probability']["neg"]*100

        rem = 100-nut

        pos = (pos * rem) / 100
        neg = (neg * rem) / 100
        #print(pos)
        #print(neg)
        return render(request,"Fi/graf.html" , {
            "nut": nut,
            "pos": pos,
            "neg":neg
        })
    else:
        return redirect("/")

def sao2(request):
    s = so()
    return HttpResponse(s)





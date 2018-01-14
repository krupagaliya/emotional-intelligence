import urllib
import urllib.request
import urllib.parse


def so():

    inp = input("Enter text")#"I am a very Good happy Lovely"

    txt = inp

    data = urllib.parse.urlencode({"text": txt}).encode("utf-8")

    u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

    the_page = u.read()

    return the_page


def sa(a,b):
    return a+b


def sen():
    return "hello wolrd i m here where r u ??"


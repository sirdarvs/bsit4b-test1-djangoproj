from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome, BSIT 4B!</h1>")

def test1(request):
    return HttpResponse("<h2>Click here!</a>")


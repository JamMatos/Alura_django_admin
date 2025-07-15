from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>Jamil</h1><p>Oh girl i like you, I do</p>')
    return render(request, 'index.html')

def post_malone(request):
    return HttpResponse('<p>Oh girl i like you, I do</p>')

from django.shortcuts import render
from django.http import HttpResponse


def helleView(request):
    return HttpResponse("Hello dars")
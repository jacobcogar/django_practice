from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.


def starting_page(request):
    return render(request, 'blog/index.html') # will render the starting page layout from template index.html

def posts(requests):
    pass

def post_detail(request):
    pass
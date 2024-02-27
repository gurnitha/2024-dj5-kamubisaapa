# app/projects/views.py

# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hallo_world(request):
	return HttpResponse(
			"<h1>Hello World!</h1>\
			<h3>Hallo Teman</h3>\
			<p>nama saya NYOMAN, pensiunan PNS</p>\
			<p>Saya bisa Django, Anda bisa apa?</p>")
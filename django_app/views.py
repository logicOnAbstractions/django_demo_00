from django.shortcuts import render
from django.http import HttpResponse        # django's HTTP, not std lib!


""" Defines all the endpoints behavior here. similarly to cherrypy, you can (I think) use decorators, and then use those as entry-points for further actions at the endpoint."""

def index(resquest):
    return HttpResponse(f"This is your servername & port: {resquest.META['SERVER_NAME']}:{resquest.META['SERVER_PORT']}")
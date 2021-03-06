from django.shortcuts import render
from django.http import HttpResponse        # django's HTTP, not std lib!
from django.template import loader
import logging
from django_demo_00.utils import *

""" Defines all the endpoints behavior here. similarly to cherrypy, you can (I think) use decorators, and then use those as entry-points for further actions at the endpoint.

    **Each of those must be defined in urlpatterns so they can get called **
    
    * the urlpattern also defines the question_id argument. see django_app/urls.py for detail 
"""
logger = logging.getLogger(CUSTOME_LOGGERNAME)

def index(request):
    """ syntaxic sugar: let's wrap the httpresponse mess into a method call  """

    from .models import Question
    from django.shortcuts import render

    latest_question_list    = Question.objects.order_by('-pub_date')
    print(latest_question_list)
    template_path           = 'django_app/index.html'
    ctx                     = {'latest_question_list':latest_question_list}

    logger.info(f"Just saying django_app/views.py index received a call... ")
    return render(request, template_path, ctx)              # thus we don't need to import Httpresponse & such anymore

def index_v1(request):
    """ an index that returns a response defined in a template. this is a way to do it, but not the best, because now we need to import the models, which means we have coupled them pretty hard....  """

    from .models import Question

    latest_question_list    = Question.objects.order_by('-pub_date')                # query the db -through out data model- to get some data
    template                = loader.get_template('django_app/index.html')          # load some template that knows what to display for those data
    ctx                     = {'latest_question_list':latest_question_list}         # a context in django has to be a dictionnary

    return HttpResponse(template.render(ctx, request))                              # a template knows how to render itself, given a context & some request

def index_v0(request):
    """ just the first endpoint we created as index for ref. """
    return HttpResponse(f"This is your servername & port: {request.META['SERVER_NAME']}:{request.META['SERVER_PORT']}")



def detail(request, question_id):
    """
     ok. but if we're going to wrap everything in else raise 404, might as well wrap this whole mess into a method
    """

    from .models import Question
    from django.shortcuts import render, get_object_or_404
    question = get_object_or_404(Question, pk=question_id)      # we get ride of the try/except since its handled in the method for us
    ctx = {'question':question}
    template_path           = 'django_app/detail.html'

    logger.info(f"Just saying django_app/views.py detail received a call... Going for a fancy template usage here.  ")

    return render(request, template_path, ctx)

def detail_v1(request, question_id):
    """
    that was nice, but we'd like to return a proper 404 if not found
    """

    from .models import Question
    from django.http import Http404
    from django.shortcuts import render

    try:
        question = Question.objects.get(pk=question_id)                 # try to find in datamodel (db) an object with our current id, question_id
    except Question.DoesNotExist:
        raise Http404(f"oups, that didn't work out well...")
    ctx = {'question':question}
    template_path           = 'django_app/detail.html'
    return render(request, template_path, ctx)

def detail_v0(request, question_id):
    """

    BASIC VERSIOn
    :param request: the rqst (with body, params etc.)
    :param question_id: a parameteres for that endpoint
    :return:
    """
    return HttpResponse(f"here are some more detials about all this, that's the question: {question_id}")

def results(request, question_id):
    """ """
    return HttpResponse(f"look at those polls! question id: {question_id}")


def vote(request, question_id ):
    """ """

    return HttpResponse(f"you're voting on question: {question_id}")

def template(request):
    """ returning our very own base template to show functionnality in django"""

    return render(request, 'django_app/base.html', {'title':"title set in views.template(rqst)", "foo":"this is the foo variable"})

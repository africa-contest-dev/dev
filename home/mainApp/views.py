# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404


def homePage(request):
    return render_to_response('landing-1.html',context_instance= RequestContext(request))

def landing(request, page_number):
    try:
        offset = int(page_number)
    except ValueError:
        raise Http404()
    html = 'landing-%s.html' % offset
    return render_to_response(html,context_instance= RequestContext(request))
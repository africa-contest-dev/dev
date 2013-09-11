# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404


country_to_flag_map = {'eg':'egypt-flag-map',
                       'ng':'nigeria-flag-map',
                       'cm':'cameroon-flag-map',
                       'ke':'kenya-flag-map',
                       'za':'south-africa-flag-map',
                       'gh':'ghana-flag-map'}


def landingPage(request):
    return render_to_response('landing-home.html', context_instance= RequestContext(request))


def homePage(request):
    return render_to_response('home.html',context_instance= RequestContext(request))


def countryPage(request, country_code):
    html = '%s-home.html' % country_code
    return render_to_response(html,context_instance= RequestContext(request))


def aboutPage(request):
    return render_to_response('about.html',context_instance= RequestContext(request))


def applyPage(request):
    return render_to_response('apply.html',context_instance= RequestContext(request))


def contactPage(request):
    return render_to_response('contact.html',context_instance= RequestContext(request))

# def landing(request, page_number):
#     try:
#         offset = int(page_number)
#     except ValueError:
#         raise Http404()
#     html = 'landing-%s.html' % offset
#     return render_to_response(html,context_instance= RequestContext(request))
from django.shortcuts import render
from speaker.models import *
from .models import *

def index(request):
    allSpeakers = Speaker.objects.filter(isAtHome=True)
    indexactive = 'current'
    allBanners = Banner.objects.filter(is_active=True).order_by('order')
    return render(request, 'staticPages/index.html', locals())

def faq(request):
    faqs = list(Faq.objects.all())
    left_faqs = faqs[0::2]
    right_faqs = faqs[1::2]
    return render(request, 'staticPages/faq.html', locals())




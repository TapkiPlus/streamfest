from django.shortcuts import render
from speaker.models import *
from .models import *
from speaker.models import Ticket,Order

def index(request):
    allSpeakers = Speaker.objects.filter(isAtHome=True)
    indexactive = 'current'
    allBanners = Banner.objects.filter(is_active=True).order_by('order')
    oneDayTicket = Ticket.objects.get(isDefaultOneDayTicket=True)
    twoDayTicket = Ticket.objects.get(isDefaultTwoDayTicket=True)
    return render(request, 'staticPages/index.html', locals())

def faq(request):
    faqs = list(Faq.objects.all())
    left_faqs = faqs[0::2]
    right_faqs = faqs[1::2]
    return render(request, 'staticPages/faq.html', locals())

def contacts(request):

    return render(request, 'staticPages/contacts.html', locals())


def order(request, pass_type):
    passArticle = pass_type
    return render(request, 'staticPages/order.html', locals())

def new_order(request):
    if request.POST:
        print(request.POST)
        customerFio = request.POST.get('username')
        customerPhone = request.POST.get('phone')
        customerEmail = request.POST.get('email')
        passArticle = request.POST.get('passArticle')

        Order.objects.create(customerFio=customerFio,customerEmail=customerEmail,customerPhone=customerPhone)
    else:
        print('GETTTT')



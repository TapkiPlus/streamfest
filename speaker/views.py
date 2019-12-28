from django.shortcuts import render, get_object_or_404
from .models import *


def speaker(request,nickNameSlug):
    curSpeaker = get_object_or_404(Speaker, nickNameSlug=nickNameSlug)
    streamersactive = 'current'
    oneDayTicket = Ticket.objects.get(isDefaultOneDayTicket=True)
    twoDayTicket = Ticket.objects.get(isDefaultTwoDayTicket=True)
    oneDayTicket_slug = f'{curSpeaker.nickNameSlug}_{oneDayTicket.article}'
    twoDayTicket_slug = f'{curSpeaker.nickNameSlug}_{twoDayTicket.article}'
    return render(request, 'speaker/speaker.html', locals())

def all_speakers(request):
    streamersactive = 'current'
    allSpeakers = Speaker.objects.all().order_by('orderPP')
    return render(request, 'speaker/speakers.html', locals())

def stats(request,code):
    streamer = get_object_or_404(Speaker, uniqUrl=code)
    return render(request, 'speaker/stat.html', locals())

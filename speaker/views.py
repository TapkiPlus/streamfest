from django.shortcuts import render, get_object_or_404
from .models import *

def speaker(request,nickNameSlug):
    curSpeaker = get_object_or_404(Speaker,nickNameSlug=nickNameSlug)
    return render(request, 'speaker/speaker.html', locals())

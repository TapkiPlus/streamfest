from django.shortcuts import render

def index(request):
    return render(request, 'staticPages/index.html', locals())

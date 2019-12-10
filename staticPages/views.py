from django.shortcuts import render

def index(request):
    indexactive = 'current'
    return render(request, 'staticPages/index.html', locals())




from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('<nickNameSlug>', views.speaker, name='speaker'),

   # path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   # path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   # # path('posts/', views.allPosts, name='allposts'),
   # # path('post/<slug>/', views.showPost, name='showpost'),
   path('all/', views.all_speakers, name='all_speakers'),
   path('stats/<code>', views.stats, name='stats'),
   # path('services/', views.services, name='services'),
   # path('service/<slug>/', views.service, name='service'),
   # path('robots.txt', views.robots, name='robots'),



]

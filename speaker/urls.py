from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('/<nickNameSlug>', views.speaker, name='speaker'),

   # path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   # path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   # # path('posts/', views.allPosts, name='allposts'),
   # # path('post/<slug>/', views.showPost, name='showpost'),
   # path('about/', views.about, name='about'),
   # path('contacts/', views.contacts, name='contacts'),
   # path('services/', views.services, name='services'),
   # path('service/<slug>/', views.service, name='service'),
   # path('robots.txt', views.robots, name='robots'),



]

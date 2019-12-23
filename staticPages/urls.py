from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('', views.index, name='index'),
   # path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   # path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   # # path('posts/', views.allPosts, name='allposts'),
   # # path('post/<slug>/', views.showPost, name='showpost'),
   path('faq/', views.faq, name='faq'),
   path('contacts/', views.contacts, name='contacts'),
   path('order/<pass_type>/', views.order, name='order'),
   path('new_order/', views.new_order, name='new_order'),
   # path('services/', views.services, name='services'),
   # path('service/<slug>/', views.service, name='service'),
   # path('robots.txt', views.robots, name='robots'),



]

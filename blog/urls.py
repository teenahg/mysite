from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog', views.blog, name = 'blog'),
    path('singleblog', views.singleblog, name = 'singleblog'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('portfoliodetails', views.portfoliodetails, name = 'portfoliodetails'),
    path('elements', views.elements, name = 'elements'),
    path('contact_process', views.contact_process, name = 'contact_process')
]
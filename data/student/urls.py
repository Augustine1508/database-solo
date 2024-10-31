from django.urls import path
from .home import HompageView, About



urlpatterns = [
    path('', HompageView.as_view(), name='homeview'),
    path('About', About, name='about')
    
   

]

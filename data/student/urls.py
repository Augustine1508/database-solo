from django.urls import path
from .home import HomepageView, About
from . import home


urlpatterns = [
    path('', HomepageView.as_view(), name='homeview'),
    # path('About', About, name='about')
    path('about/<int:student_id>/', home.AboutView.as_view(), name='about'),
   

]



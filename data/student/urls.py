from django.urls import path
from .home import student_list

# from .home import HompageView


# urlpatterns = [
#     path('', HompageView.as_view(), name='homeview')
    
   

# ]

urlpatterns = [
    path('', student_list, name='student-list')
]

from django.shortcuts import render
from django.views.generic import View

from .models import Student, Student_Profile, Program, CohortGroup


class HompageView(View):
    def get(self, request):
        all_students = Student.objects.all()
        context = {
            'students': all_students
        }


        return render(request, 'html/main.html',
        context = context)



# class AboutView(View):
#     def get(self, request):
#         all_students = Student.objects.all()
#         context = {
#             'students': all_students
#         }


#         return render(request, 'html/about.html',
#         context = context)


def About(request):
    return render(request, 'html/about.html')
    


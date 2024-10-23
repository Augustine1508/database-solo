from django.shortcuts import render
from django.views.generic import View
from .models import Student, Student_Profile, Program, CohortGroup


# class HompageView(View):
#     def get(self, request):
#         return render(request, 'html/main.html')
    

def student_list(request):
    students = Student.objects.all()
    profiles = Student_Profile.objects.all()
    programs = Program.objects.all()

    return render(request, 'html/tryout.html', {
        'students': students,
        'profiles': profiles,
        'program': programs,
    })
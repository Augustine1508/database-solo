from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from .models import Student, Student_Profile, Program, CohortGroup


class HomepageView(View):
    def get(self, request):
        all_students = Student.objects.all()
        context = {'students': all_students}
        
        paginator = Paginator(Student.objects.all(), 3)
        page = request.GET.get('page')
        students = paginator.get_page(page)

        return render(request, 'html/main.html', context=context)




class AboutView(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        context = {'student': student}
        return render(request, 'html/about.html', context, )






# class HompageView(View):
#     def get(self, request):
#         all_students = Student.objects.all()
#         context = {
#             'students': all_students
#         }


#         return render(request, 'html/main.html',
#         context = context)



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
    


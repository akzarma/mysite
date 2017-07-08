# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView

import datetime
from django.http import HttpResponse, HttpResponseRedirect

from .models import Student
from django.shortcuts import render
from .forms import StudentForm


# Create your views here.


def home(request):

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        print(form.fields['doc_profile_pic'])
        if form.is_valid():
            student = form.save()
            print("save")
            context = {'submit_check': 1, 'basic_form': StudentForm(initial={'gr_number': '55564', 'handicapped': False, 'jee_total': 120})}
            print(context.values())
        else:
            print("else")
            context = {'submit_check': 0, }
            print(context.values())

        return render(request, 'test/index.html', context)

    else:
        context = {
            'basic_form': StudentForm(initial={'gr_number': '55564', 'handicapped': False, 'jee_total': 120}),
        }

        return render(request, 'test/index.html', context)




def action(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob_s = (request.POST.get('dob'))
        mobile = int(request.POST.get('number'))
        print(name + email + dob_s + str(mobile))
        dob_d = datetime.datetime.strptime(dob_s, "%Y-%m-%d").date()
        new_student = Student(name=name, email=email, mobile=mobile, DOB=dob_d)
        new_student.save()
        return HttpResponseRedirect('/action/')
    else:
        return HttpResponse("Refresh")


def test(request):
    template_name = 'test/all_students.html'
    return render(request, 'test/all_students.html', {
        'root': settings.MEDIA_ROOT,
        'all_students': Student.objects.all()
    })


# class DetailView(generic.ListView):
#     context = {
#         'root': settings.MEDIA_ROOT,
#         'all_students': Student.objects.all()
#     }
#
#     # context_object_name = 'all_students'  # optional...to override default object name object_list
#     def get_queryset(self):
#         return render()

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('home:all_students')



def DetailView(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'test/details.html', {'student': student, 'basic_form': StudentForm()})


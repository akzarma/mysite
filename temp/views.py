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
            context = {'submit_check': 1, 'basic_form': StudentForm(
                initial={'gr_number': '55564', 'handicapped': False, 'jee_total': 120})}
            print(context.values())
        else:
            print("else")
            context = {'submit_check': 0, }
            print(context.values())
            print(form.errors)
        return HttpResponseRedirect('/test/')

    else:
        context = {
            'basic_form': StudentForm(initial={'gr_number': '55564', 'handicapped': False, 'jee_total': 120}),
        }

        return render(request, 'test/index.html', context)


def login(request):
    return render(request, 'test/login.html')





def grid_view(request):
    return render(request, 'test/all_students_grid.html', {
        'root': settings.MEDIA_ROOT,
        'all_students': Student.objects.all()
    })


def list_view(request):
    return render(request, 'test/all_students_list.html', {
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

# class StudentDelete(DeleteView):
#     model = Student
#     success_url = reverse_lazy('home:all_students_list')


def detail_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'test/details.html', {'student': student, 'basic_form': StudentForm()})


def update(request, student_id):
    # return HttpResponse("Hi")
    student = get_object_or_404(Student, pk=student_id)
    print(student.doc_jee_marksheet.url)
    return render(request, 'test/update.html', {'basic_form': StudentForm(instance = student)})

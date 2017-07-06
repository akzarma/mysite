# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from zope.interface.tests.test_interfaces import _ConformsToIObjectEvent

from .models import Student
from django.shortcuts import render
from .forms import StudentForm


# Create your views here.


def home(request):
    # s = Student(name="Dweep",marks=1)
    # s.save()
    #saves student details
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("save")
            return HttpResponseRedirect('/test/')
        else:
            print("else")
            return HttpResponse(form.errors.as_data())
    else:
        context = {
            'basic_form' : StudentForm(initial={'gr_number':'555','handicapped':False}),
        }


        # print(form)
        print("3")
        return render(request, 'test/index.html',context)



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



class DetailView(generic.ListView):
    template_name = 'test/details.html'

    context_object_name = 'all_students' #optional...to override default object name object_list

    def get_queryset(self):
        return Student.objects.all()



# ignore niche wala!!

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name',
              'middle_name',
              'last_name',
              'DOB',
              'admission_type',
              'shift',
              'caste_type',
              'branch',
              'gr_number',
              'email',
              'mobile',
              'religion',
              'sub_caste',
              'handicapped',
              'nationality',
              'emergency_name',
              'emergency_mobile',
              'emergency_relation',
              'emergency_address',
              'father_name',
              'father_profession',
              'father_designation',
              'father_mobile',
              'father_email',

              'mother_name',
              'mother_profession',
              'mother_designation',
              'mother_mobile',
              'mother_email',
              'permanent_address',
              'permanent_state',
              'permanent_city',
              'permanent_pin_code',
              'permanent_country',

              'current_address',
              'current_state',
              'current_city',
              'current_pin_code',
              'current_country',
              'jee_physics',
              'jee_maths',
              'jee_chemistry',
              'jee_total',
              'jee_max_physics',
              'jee_max_maths',
              'jee_max_chemistry',
              'doc_tenth_marksheet',
              'doc_twelfth_marksheet',
              'doc_jee_marksheet',
              ]
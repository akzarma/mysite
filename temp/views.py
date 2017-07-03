# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.shortcuts import render
from .forms import StudentForm


# Create your views here.


def home(request):
    # s = Student(name="Dweep",marks=1)
    # s.save()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.data['name']
            DOB = form.data['DOB']
            email = form.data['email']
            mobile = form.data['mobile']
            marks = request.FILES['marks']
            if marks.size > 5 * 1024 * 1024:
                return HttpResponse("File size too big" + str(marks.size))
            # marks
            new_student = Student(name=name, DOB=DOB, email=email, mobile=mobile, marks=marks)
            new_student.save()
            print("save")
            return HttpResponseRedirect('/test/')
        else:
            print("else")
            return HttpResponse(form.errors.as_data())
    else:
        form = StudentForm()

    return render(request, 'index.html',
                  {
                      'forms': form
                  })


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

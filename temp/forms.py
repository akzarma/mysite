from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Enter Name')
    DOB = forms.DateField(label='Enter DOB')
    email = forms.EmailField(label='Enter Email')
    mobile = forms.IntegerField(label='Enter Mobile')
    marks = forms.FileField(label='Select a File')
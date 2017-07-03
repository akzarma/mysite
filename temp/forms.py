from django import forms
from .validators import file_size_validators


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter Name')
    DOB = forms.DateField(label='Enter DOB')
    email = forms.EmailField(label='Enter Email')
    mobile = forms.IntegerField(label='Enter Mobile')
    marks = forms.FileField(label='Select a File', validators=[file_size_validators])

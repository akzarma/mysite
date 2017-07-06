from django import forms
from .validators import file_size_validators
from .models import Student


class StudentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({
    #         'class':'col-md-2'
    #     })
    # for field in iter(self.fields):
    #     self.fields[field].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    class Meta:
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

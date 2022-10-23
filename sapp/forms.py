from django import forms
from .models import Student
class StudentForm(forms.Form):
    name = forms.CharField(max_length=30)
    sclass = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    school = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)

class SForm(forms.Form):
    name = forms.CharField(max_length=30)


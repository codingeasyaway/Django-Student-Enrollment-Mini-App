from django.shortcuts import render ,HttpResponse

# Create your views here.
# Home Page
from .forms import StudentForm, SForm
from .models import Student


def Index(request):
    return render(request, 'index.html')

# Register Page
def Register(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        sclass = form.cleaned_data['sclass']
        address = form.cleaned_data['address']
        school = form.cleaned_data['school']
        email = form.cleaned_data['email']
        student = Student(name=name, sclass=sclass, address=address, school=school, email=email)
        student.save()

    return render(request, 'register.html', {'form': form})

# Existing
def Existing(request):
    queryset = Student.objects.all()
    return render(request, 'existing.html', {'queryset': queryset})


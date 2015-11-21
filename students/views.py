from django.shortcuts import render
from .models import Student  #to import the Students Model
from django.views.generic.edit import CreateView , UpdateView
# Create your views here.

class StudentRegister(CreateView):
    #to use the models variable
    model = Student
    #we require all fields since students will need register him/her self
    fields = '__all__'
    template_name = "Student_Profile_Create.html"
    #after succeding in the registery proccess the student will be redirected to this directery
    success_url = ("Home",)

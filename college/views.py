# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from college.models import StudentApplication, Department, StudentRegistration, StaffRegistration, TimeStampModel
# Create your views here.


def home(request):
    return render(request, 'college/home.html')


def student_application(request):
    if request.method == "POST":
        StudentApplication.objects.create(
            student_name=request.POST['student-name'],
            email=request.POST['email'],
            dob=request.POST['dob'],
            ssc_doc=request.FILES['ssc-doc'],
            inter_doc=request.FILES['inter-doc'],
        )
        return HttpResponseRedirect(reverse('college:home'))
    return render(request, 'college/student-application.html', {})


def student_registration(request):
    if request.method == "POST":
        email = request.POST['email']
        student_app = StudentApplication.objects.get(email=email, is_verified=True)
        user_object = User.objects.create_user(username=request.POST['username'],
                                               first_name=request.POST['first-name'],
                                               last_name=request.POST['last-name'],
                                               email=request.POST['email'],
                                               password=request.POST['password']
                                               )
        dept = Department.objects.create(department_name=request.POST['department'])
        if student_app.email == user_object.email:
            StudentRegistration.objects.create(
                application=student_app,
                user=user_object,
                father_name=request.POST['father-name'],
                mother_name=request.POST['mother-name'],
                profile_pic=request.FILES['profile-pic'],
                gender=request.POST['gender'],
                nationality=request.POST['nationality'],
                department=dept
            )
            return HttpResponseRedirect(reverse('college:home'))
        return render(request, 'college/student-registration.html', {})
    return render(request, 'college/student-registration.html', {})


def staff_registration(request):
    if request.method == "POST":
        user_object = User.objects.create_user(username=request.POST['username'],
                                               first_name=request.POST['first-name'],
                                               last_name=request.POST['last-name'],
                                               email=request.POST['email'],
                                               password=request.POST['password']
                                               )
        dept = Department.objects.create(
            department_name=request.POST['department']
        )
        StaffRegistration.objects.create(
            user=user_object,
            gender=request.POST['gender'],
            age=request.POST['age'],
            salary=request.POST['salary'],
            profile_pic=request.FILES['profile-pic'],
            nationality=request.POST['nationality'],
            department=dept
        )
        return HttpResponseRedirect(reverse('college:home'))
    return render(request, 'college/staff-registration.html', {})


# def login_view(request):
#     if request.method == "POST":
#         email=request.POST['email']
#         password=request.POST['password']
#         user=authenticate(request, email=email, password=password):
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect()

from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

def home(request):
    data = User.objects.all()
    if request.method == 'POST':
        add_form = StudentRegistration(request.POST)
        if add_form.is_valid():
            name = add_form.cleaned_data['name']
            email = add_form.cleaned_data['email']
            password = add_form.cleaned_data['password']
            stu_data = User(name=name, email=email, password=password)
            stu_data.save()
    else: 
        add_form = StudentRegistration()
    context = {
        'add_from':add_form,
        'data':data
    }
    return render(request, 'enroll/home.html', context)

def update(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id) 
        up_form = StudentRegistration(request.POST, instance=data)
        if up_form.is_valid():
            up_form.save()  
    else:
        data = User.objects.get(pk=id) 
        up_form = StudentRegistration(instance=data)
    context = {
        'up_form':up_form,
    }
    return render(request, 'enroll/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return redirect ('home')



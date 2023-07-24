from django.shortcuts import render, redirect, HttpResponse
from intern.models import internregister
from django.contrib.auth import logout,login
from django.contrib.auth.hashers import check_password

# Create your views here.
def home(request):
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        Phone_number = request.POST['Phone_number']
        Email = request.POST['Email']
        Linkedin_Link = request.POST['Linkedin_Link']
        Github_Link = request.POST['Github_Link']
        Skills = request.POST['Skills']
        password = request.POST['password']

        user = internregister.objects.create(name=username,
                                             phone=Phone_number,
                                             email=Email,
                                             Linkedin_Link=Linkedin_Link,
                                             Github_Link=Github_Link,
                                             Skills=Skills,
                                             password=password)
        user.save()
        return redirect(home)
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = internregister.objects.get(name=username, password=password)
        print(user.password)
        print(password)
        if user and user.password == password:
            request.session['uid'] = user.id
            print("success")
            return render(request, 'intern_dashboard/index.html')
        else:
            return HttpResponse("error")
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login_view')


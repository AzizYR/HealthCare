from django.shortcuts import render
from .models import db
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def single(request):
    return render(request , 'home/single.html')

def about(request):
    return render(request, 'home/about.html')


def appointment(request):
    return render(request, 'home/appointment.html')


def contact(request):
    return render(request, 'home/contact.html')


def gallery(request):
    return render(request, 'home/gallery.html')

def register(request):
    name = request.POST['regname']
    email = request.POST['regemail']
    password = request.POST['regpassword1']
    print(name)

    obj = db(name = name , email = email , password = password)
    print(obj)
    obj.save()

    return render(request , 'home/index.html')


def dashboard(request):
    name = request.POST['name']
    password = request.POST['password']
    dataset =db.objects.all()
    datasetadmin = dbadmin.objects.all()
    if(name is not "admin"):
        try:
            find = dataset.get(name = name)
            print("Found")
            if(password == find.password):
                pass
            else:
                return render(request , 'home/index.html' )

        except Exception as e:
            return render(request , 'home/index.html' )
    else:
        if(password is "admin"):
            return HttpResponse("<a href = http://192.168.1.139:8000/admin/>Admin Access Granted Here!</a>")
        else:
            return HttpResponse("<h1>Access Denied</h1>")

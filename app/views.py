from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        branch=request.POST.get('branch')
        print(name,email,age,gender,branch)
        query=Student(name=name,email=email,age=age,gender=gender,branch=branch)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
        
    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        branch=request.POST['branch']
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.branch=branch
        edit.save()
        messages.info(request,"Data Updated Successfully")

        return redirect("/")

    d=Student.objects.get(id=id)
    print(d)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")

    return redirect("/")

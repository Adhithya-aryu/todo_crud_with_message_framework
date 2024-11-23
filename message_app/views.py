from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import todoForm
from .models import todo
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def update(request,id):
    task = todo.objects.get(id = id )
    if request.method == "POST":
        form = todoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Your old task has been updated successfully !!")
            return redirect("all")
    else:
        form = todoForm(instance=task)
    
    return render(request,"update.html",{"form":form})

def add(request):
    form = todoForm()
    
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your new task has been created successfully !!")
            return redirect("all")
        else:
            form = todoForm()
    return render(request,"add.html",{"form":form})

def all(request):
    objects = todo.objects.all()
    return render(request, "all.html",{"tasks":objects})

def delete(request,id):
    delete_data = get_object_or_404(todo,id=id)
    delete_data.delete()
    messages.error(request, "task has been deleted successfully !!")
    return redirect("all")



from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all(),
    }
    return render(request, "page.html", context)

def make_new_dojo(request):
    Dojo.objects.create(
        name=request.POST['dojo_name'],
        city=request.POST['city'],
        state=request.POST['state'],
        description=request.POST['description']
    )
    return redirect('/')

def make_new_ninja(request):
    dojo = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = dojo
    )
    return redirect('/')

def delete_dojo(request, dojo_id):
    current_dojo = Dojo.objects.get(id=dojo_id)
    current_dojo.delete()
    return redirect('/')
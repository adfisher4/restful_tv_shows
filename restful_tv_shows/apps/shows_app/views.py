from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    print(50 * '*')

    return render(request, 'index.html', context)

def new_show(request):
    if request.method == "POST":
        Show.objects.create(name=request.POST['name'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        return redirect('/shows/')
    
    else:
        return render(request, 'new_show.html')

def view_show (request, id):

    context = {   
        'chosen': Show.objects.get(id=id),
    }
   
    return render(request, 'view_show.html', context)

def edit_show_page(request, id):
    context = {   
        'chosen': Show.objects.get(id=id)
        }
    return render(request, 'edit_show.html', context)

def edit_show(request, id):
    if request.method == "POST":
        show_to_edit = Show.objects.get(id=id)
        show_to_edit.name = request.POST['name']
        show_to_edit.network=request.POST['network']
        show_to_edit.release_date=request.POST['release_date']
        show_to_edit.description=request.POST['description']
        show_to_edit.save()
        return redirect (f'/shows/view_show/{id}')  


def delete_show (request, id):
    if request.method == "GET":
        chosen = Show.objects.get(id=id)
        chosen.delete()

        return redirect('/shows/')

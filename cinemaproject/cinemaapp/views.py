from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from.forms import Movie_Form
# Create your views here.
def test(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)
def detail(request,film_id):
    details=movie.objects.get(id=film_id)
    return render(request,'details.html',{'details':details})
def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['image']
        add=movie(name=name,des=des,year=year,image=img)
        add.save()
    return render(request,'add.html')

def update(request,id):
    Mov=movie.objects.get(id=id)
    form=Movie_Form(request.POST or None,request.FILES,instance=Mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form_key':form,'Movie':Mov})

def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')

from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food

def index(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FoodForm()
    return render(request, 'insert.html', {'fo': form})
def show(request):
    a=Food.objects.all()
    return render(request,'show.html',{'view_data':a})

def upda(request,food_id):
    s=Food.objects.get(food_id=food_id)
    if request.method=='POST':
        v = request.POST['nam']
        b = request.POST['qty']
        c = request.POST['price']
        s.food_name = v
        s.qty = b
        s.price = c
        s.save()
        return redirect('sh')
    return render(request,'update.html',{'k': s})

def dele(request,food_id):
    s = Food.objects.get(food_id=food_id)
    s.delete()
    return redirect('sh')
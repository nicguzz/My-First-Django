from django.shortcuts import redirect, render
from .models import Order
from .form import TransacaoForm


meals = {
    "Cheeseburguer": 10,
    "Hot dog": 5,
    "Pizza": 7,
    "T-Bone": 20,
    "French fries": 3,
    "Salmon tartar": 15
    }

def index(request):


        
    return render(request, 'index.html', {'meals': meals})

 
def list(request):
    data = {}
    data['list'] = Order.objects.all()

    return render(request, 'list.html', data)

def new_order(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    data['form'] = form

    return render(request, 'form.html', {'data':data, 'meals':meals})


def order2(request):
    id = request.POST['id_form']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    meal = request.POST['meal']
    curso = Order.objects.create(id=id, first_name=first_name, last_name=last_name, age=age, meal=meal)

    return redirect('list')

def delete(request, id):
    curso = Order.objects.get(id=id)
    curso.delete()

    return redirect('list')

def edit(request, id):
    curso = Order.objects.get(id=id)

    return render(request, "edit.html", {"curso": curso})


def edited(request):
    id = request.POST['id_form']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    meal = request.POST['meal']

    curso = Order.objects.get(id=id)
    curso.first_name = first_name
    curso.last_name = last_name
    curso.age = age
    curso.meal = meal
    curso.save()

    return redirect('list')


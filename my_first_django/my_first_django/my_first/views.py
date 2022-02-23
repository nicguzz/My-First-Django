from cgitb import html
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

    return render(request, 'form.html', data)
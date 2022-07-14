from django.forms import ModelForm
from .models import Order

class TransacaoForm(ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'age', 'meal']
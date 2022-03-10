from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list', views.list, name = 'list'),
    path('form', views.new_order, name = 'form'),
    path('edit/<id>', views.edit, name='edit'),
    path('edited', views.edited, name='edited'),
    path('delete/<id>', views.delete),
    path('order2', views.order2, name = 'order2')

]
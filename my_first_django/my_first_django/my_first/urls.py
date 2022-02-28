from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list', views.list, name = 'list'),
    path('form', views.new_order, name = 'form'),
    path('edit/<id>', views.edit),
    path('edited/<id>', views.edited),
    path('delete/<id>', views.delete),
    path('list2', views.list2, name='list2')

]
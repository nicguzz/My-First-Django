from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list', views.list, name = 'list'),
    path('form', views.new_order, name = 'form'),
    path('delete/<id>', views.delete)



]
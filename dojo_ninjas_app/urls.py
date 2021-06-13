from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('make_new_dojo',views.make_new_dojo),
    path('make_new_ninja',views.make_new_ninja),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo),
]
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
        path('', views.read),
        path('read', views.read),
        path('emp', views.create),
        path('delete/<int:id>', views.destroy),
        path('edit/<int:id>', views.edit),
        path('update/<int:id>', views.update),
]

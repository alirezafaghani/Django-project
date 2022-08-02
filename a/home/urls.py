from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'Home'),
    path("hello/", views.say_hello),
    path('detail/<int:id>/', views.detail, name = 'details'),
    path('delete/<int:id>/', views.delete, name = "delete"),
    path('kaka/<int:id>/',   views.kaka, name = "kaka"),
    path('create/', views.create, name = 'create'),
    path('update/<int:id>/', views.update, name = "update"),
]
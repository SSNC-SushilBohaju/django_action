from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('test/', views.members, name='members'),
    path('test/details/<int:id>',views.details,name='details'),
] 
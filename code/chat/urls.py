from django.urls import path

from . import views

urlpatterns = [
    path('login/<str:device>/', views.index, name='index'),
    path('run/<str:room_name>/', views.room, name='room'),
]

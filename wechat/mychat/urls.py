from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<int:id>', views.chat, name='chat'),
    path('friends/', views.friends, name='friends'),
]

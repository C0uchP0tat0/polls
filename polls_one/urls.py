from django.urls import path, include
from . import views

urlpatterns = [
    #path('', IndexView.as_view(), name='index')
    path('', views.HomePage.as_view(), name='home'),
    #path(r'^detail/<int:pk>/$', views.DetalePage.as_view(), name='detail'),
    
    path('detail/<int:pk>/', views.DetalePage.as_view(), name='detail'),
]

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.MainIndexView.as_view(), name='index'),
    path('add/', views.AppLoginPasswordView.as_view(), name='add'),
    path('<str:appinfo>/', views.LoginPasswordView.as_view(), name='loginspasswords'),
    path('update/<int:id_l>/', views.loginpasswordedit, name='update')
]
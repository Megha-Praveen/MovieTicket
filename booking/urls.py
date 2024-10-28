from django.contrib import admin
from django.urls import path
from.views import login, register, book, payment, logout
from.import views 

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('book',views.book,name="book"),
    path('payment',views.payment,name="payment"),
    path('logout',views.logout,name="logout"),
]
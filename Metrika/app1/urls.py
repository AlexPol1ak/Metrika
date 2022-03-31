from django.urls import path
from . import views

urlpatterns = [
               path('', views.home),# Стартавая страница
               path('reg/', views.reg), #  Страница регистрации
               path('mypage/', views.mypage), # Личная страница
               path('wash/', views.wash), #  Страница удаления данных
               path('home/', views.home) # Домашнаяя страница
]
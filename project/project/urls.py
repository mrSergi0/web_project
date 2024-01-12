"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as main_views # импортируем views из папки main

# Здесь мы описываем конфигурации тех урл, которые юзер будет использовать для взаимодейтсвия с сайтом!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_views.test), # прописываем путь к функции test в папке main в файле views. Теперь по запросу url main_page/ должна сработать функция test.
    path('', main_views.test), # таким образом страницу main_page можно сделать стартовой.В пути(первый параметр) оставляем пустую строку.
]

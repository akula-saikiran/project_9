"""
URL configuration for project_9 project.

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
from productapp.views import HomeView,InsertInput,InsertView,DisplayView,UpdateInput,UpdateView,DeleteView,DeleteInput

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('home/insert/', InsertInput.as_view()),
    path('home/insert/insertinput/',InsertView.as_view()),
    path('home/display/',DisplayView.as_view()),
    path('home/update/',UpdateInput.as_view()),
    path('home/update/updateinput',UpdateView.as_view()),
    path('home/delete/',DeleteInput.as_view()),
    path('home/delete/deleteinput/',DeleteView.as_view()),

]

"""
URL configuration for API_practice project.

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
from todos.views import TodoList, TodoDetail, DoneList, DoneTodo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos/", TodoList.as_view(), name='todo-list'),
    path("todos/<int:pk>/", TodoDetail.as_view(), name='todo-detail'),
    path("done/", DoneList.as_view(), name='todo-done'),
     path("done/<int:pk>/", DoneTodo.as_view(), name='todo-complete'),
]

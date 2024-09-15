"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from app.views import (
    MainPageView,
    UserRegistrationView,
    TrainVariationsView,
    MaterialsView,
    SearchView,
    ForumView,
    AccountView,
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register_user'),
    path('train_variations/', TrainVariationsView.as_view(), name='train_variations'),
    path('materials/', MaterialsView.as_view(), name='materials'),
    path('search/', SearchView.as_view(), name='search'),
    path('forum/', ForumView.as_view(), name='forum'),
    path('account/', AccountView.as_view(), name='account'),
]

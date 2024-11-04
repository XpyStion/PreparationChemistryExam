from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from app.base.views_base import ViewBase
from app.forms import UserRegistrationForm, LoginForm
from app.models import Roles


class MainPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'main_page/main_page.html')


class UserRegistrationPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')
    INVALID_FORM_ERROR: str = 'Invalid form data provided'

    @staticmethod
    def get(request):
        form = UserRegistrationForm()
        return render(request, 'account/register_user.html', {'form': form})

    @staticmethod
    def post(request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'account/register_user.html', {'form': form})


class TrainVariationsPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'train_variations/train_variations.html')


class MaterialsPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'materials/materials.html')


class SearchPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'search/search.html')


class ForumPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'forum/create_task.html')


class AccountPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return render(request, 'account/account.html')


class LoginPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'account/login.html')

    @staticmethod
    def post(request):
        form = LoginForm(request, request.POST)
        if not form.is_valid():
            return render(request, 'account/login.html')

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account/')


class CreateTaskView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return redirect('/login/')

        if request.user.role not in (Roles.ADMIN, Roles.TEACHER):
            return HttpResponseForbidden()

        return render(request, 'create_task/create_task.html')

    @staticmethod
    def post(request):
        if not request.user.is_authenticated:
            return redirect('/login/')

        if request.user.role not in (Roles.ADMIN, Roles.TEACHER):
            return HttpResponseForbidden()

        text_to_insert = 'TEST TEST TEST'
        context = {
            'task_text': text_to_insert,
        }
        return render(request, 'create_task/create_task.html', context)

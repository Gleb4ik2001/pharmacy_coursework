from django.shortcuts import render,redirect
from django.views import View

from django.http.response import HttpResponse
from django.http.request import HttpRequest

from django.contrib.auth import authenticate, login

from .forms import (
    SignUpForm,
    LoginForm
)
from django.contrib import messages



class SignUpView(View):
    template_name = 'signup.html'

    def get(self,request:HttpRequest)->HttpResponse:
        form = SignUpForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form':form
            }
        )

    def post(self,request:HttpRequest)->HttpResponse:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_view')
    
class LoginView(View):
    template_name = 'login.html'
    
    def get(self,request:HttpRequest)->HttpResponse:
        form = LoginForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form':form
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect('main_view')  # Поменяйте 'home' на имя вашего представления для главной страницы
            else:
                messages.error(request, 'Неправильный email или пароль.')
                return render(
                    request=request,
                    template_name=self.template_name,
                    context={
                        'form': form
                    }
                )
        else:
            messages.error(request, 'Неверный email или пароль.')
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    'form': form
                }
            )
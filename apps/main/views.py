from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import Product

class MainView(View):
    template_name = 'index.html'
    def get(self,request:HttpRequest)->HttpResponse:
        products = Product.objects.all()

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'products':products
            }
        )

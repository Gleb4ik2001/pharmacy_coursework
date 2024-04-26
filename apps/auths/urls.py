from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    SignUpView,
    LoginView
)

urlpatterns = [
    path('registration/', SignUpView.as_view(),name='signup_view'),
    path('login/',LoginView.as_view(),name='login_view')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
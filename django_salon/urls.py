"""
URL configuration for django_salon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.i18n import set_language
from base import views as base_views
from calendar_app import views as calendar_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.home, name='home'),
    path('about/', base_views.about, name='about'),
    path('products/', base_views.products, name='products'),
    path('contact/', base_views.contact, name='contact'),
    path('all_events/', calendar_views.all_events, name='all_events'),
    path('calendar/', calendar_views.view_calendar, name='calendar'),
    path('signup/', calendar_views.SignUpView.as_view(), name='signup'),
    path('login/', calendar_views.login, name='login'),
    path('user_info/', calendar_views.user_info, name='user_info'),
    path('auth/', include("django.contrib.auth.urls")),
    path('set_language/', set_language, name='set_language'),
    path('captcha/', include('captcha.urls')),
]

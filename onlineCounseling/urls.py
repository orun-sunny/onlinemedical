"""onlineCounseling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from counseling import views as user_views
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counseling.urls')),
    path("signlog/",user_views.signlog, name="signlog"),
    path("log/",auth_views.LoginView.as_view(template_name='counseling/log.html'), name="log"),
    path("logout/",auth_views.LogoutView.as_view(template_name='counseling/base.html'), name="logout"),

    path('chat/', TemplateView.as_view(template_name="chat/home.html")),
    path('messages/', include('chat.urls')),



]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.views.generic import ListView,DetailView
from django.urls import path,re_path,include
from . import views
app_name='main'

urlpatterns = [
    #path('home',views.homepage,name='homepage'),
    path('',views.intro,name='intro'),
    #re_path(r'^blog',include('blog.urls')),    
    #path('blog', include('blog.urls')),
    path('register',views.register,name='register'),
	path('logout',views.logout_request,name='logout'),
	path('login',views.login_request,name='login'),
    path('user',views.userhomepage,name='userhomepage'),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('<single_slug>',views.single_slug,name='single_slug'),



]

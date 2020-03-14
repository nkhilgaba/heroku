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
from django.contrib import admin
from django.urls import path,re_path,include
from filebrowser.sites import site
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm


from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('admin', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('blog/',include('blog.urls')),
    #re_path(r'^blog/',include('blog.urls')),  
    #path('password_reset/',include('password_reset.urls')),
    #path('password-reset',PasswordResetView.as_view(template_name='main/password_reset_form.html')),  
    path('',include('main.urls')),
    path('',include('django.contrib.auth.urls')),
    #path('reset-password/done',password_reset_done,name='reset_password_done'),
    #path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/',password_reset_confirm,name='reset_password_confirm'),

    path('tinymce', include('tinymce.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
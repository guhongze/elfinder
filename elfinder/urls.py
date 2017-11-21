"""elfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.contrib.admin.views.decorators import staff_member_required
from elfinder.views import ElfinderConnectorView,finder
from django.contrib.auth.decorators import login_required
import django
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from distutils.version import StrictVersion
from django.contrib.auth.views import LoginView,LogoutView    

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login_required(finder.as_view()),name='index'),
    url(r'^accounts/login/$', LoginView.as_view(template_name='admin/login.html'),name='login'),
    url(r'^accounts/logout/$',LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),      
    url(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$',staff_member_required(ElfinderConnectorView.as_view()),name='yawdElfinderConnectorView'),    
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }),
    ]
"""investments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
from django.contrib.auth import views as auth_view
from django.shortcuts import render
from . import views
from homedata.views import index as homedata_index, login_bar as homedata_loginbar, profile as profile
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'(?i)^mse/', include('mse.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^login_bar', homedata_loginbar, name='loginbar'),
    url(r'^login', auth_view.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout', views.lgd_out, name='logout'),
    url(r'^loggedin/', views.lgd_in),
    url(r'^account/', profile, name='account'),
    url(r'^register/', views.register, name='register'),
    url(r'^$', homedata_index),
    url(r'^.well-known', views.haqqalla),
]

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ]

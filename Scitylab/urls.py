"""Scitylab URL Configuration

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
from website import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^html/$', views.home),
    url('^login/', views.login, name='login'),
    url('^logout/$', views.logout),
    url('^sigup/$', views.sigup),
    url('^info/$', views.info),
    url('^html/news/$', views.news),
    url('^html/news/pm6/$', views.pm6),
    url('^html/news/pmc1/$', views.pmc1),
    url('^html/download/$', views.download),

]

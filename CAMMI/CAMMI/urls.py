"""CAMMI URL Configuration

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
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/secret-text/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^(?P<account_id>[0-9]+)/consumer/', include('consumer.urls')),
    url(r'^(?P<account_id>[0-9]+)/', include('account.urls')),
    url(r'^security/', include('security.urls')),
    url(r'^', include('security.urls')),
]

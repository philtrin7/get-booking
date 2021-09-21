"""getbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url

from getbooking.core import views as core_views
from getbooking.customer import views as customer_views

customer_urlpatterns = [
    path('appointment/', customer_views.appointment, name='appointment'),
    path('verify-mobile/', customer_views.verify_mobile)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home),
    path('book/', include((customer_urlpatterns, 'customer'))),
    url(r'^doctor/philtrin/([1-2][0-9]{3})-([0-1][0-9])-([0-3][0-9])/?$',
        core_views.view_week),
]

"""LearnDjango URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from book.views import sayHelloAt20200626
from book.views import indexPage
from book.views import showBooks
from book.views import bookDetail

urlpatterns = [
    url(r'^sayHelloAt20200626$', sayHelloAt20200626),
    url(r'^indexPage$', indexPage),
    url(r'^showBooks$', showBooks),
    url(r'^bookDetail/(\d+)$', bookDetail),

]

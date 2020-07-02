from django.urls import path, include
from django.contrib import admin
from . import views
'''
@Author: joker.zhang
@Date: 2020-06-22 18:00:01
@LastEditors: joker.zhang
@LastEditTime: 2020-07-02 19:00:21
@Description: For Automation
'''
"""testPlatform URL Configuration

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


urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('testcase/', include('tpTest.urls')),
]

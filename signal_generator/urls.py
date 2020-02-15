"""signal_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import datetime

from background_task import background
from background_task.models import CompletedTask, Task
from django.contrib import admin
from django.urls import path

from signals.run import run

urlpatterns = [
    path('admin/', admin.site.urls),
]

try:
    CompletedTask.objects.all().delete()
    Task.objects.all().delete()
    run(0)
except:
    print("exception")

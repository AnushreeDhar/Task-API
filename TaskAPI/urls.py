"""TaskAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from rest_framework import routers

from rest_framework.routers import DefaultRouter #SimpleRouter
from TaskApp.views import TaskViewSet #DueTaskViewSet, CompletedTaskViewSet)
#from django.core.exceptions import ImproperlyConfigured

from django.conf import settings
from django.conf.urls.static import static
from TaskApp import views


router = DefaultRouter()
#router = SimpleRouter(trailing_slash=False)
router.register(r'task', TaskViewSet, base_name="task")
#router.register(r'due_task', DueTaskViewSet)
#router.register(r'completed_task', CompletedTaskViewSet)


urlpatterns = [
   
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^register/$', views.CreateUserView.as_view(), name ='user' )
    
        
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#USE EITHER URLPATTERNS+= STATIC[]

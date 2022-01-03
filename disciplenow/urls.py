"""disciplenow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from django.urls.conf import include
from rest_framework import routers
from disciplenowapi.views import lead_dashboard, selected_disciple, DiscipleView, MessageView, disciple_home
router = routers.DefaultRouter(trailing_slash=False)
router.register("disciples", DiscipleView, "disciple")
router.register("messages", MessageView, "message")
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('lead-dashboard', lead_dashboard),
    path('disciple-home', disciple_home),
    path('selected-disciple/<slug:pk>', selected_disciple)
]

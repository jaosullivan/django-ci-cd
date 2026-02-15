from django.contrib import admin
from django.urls import path
from app.views import health, home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('new/', admin.site.urls),
    # path('api/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from todoapp.urls import router as todoapp_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(todoapp_router.urls)),
]

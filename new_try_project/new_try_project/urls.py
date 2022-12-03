from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('new_try_app/', include('new_try_app.urls')),
    path('admin/', admin.site.urls),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/', include('myapp.urls')),   # 👈 app-level URLs
]

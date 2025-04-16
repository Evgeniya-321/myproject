from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Путь к основным URL вашего приложения
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные URL для аутентификации (включает login, logout, password_change и т.д.)
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')),
    # Esta linha adiciona login, logout, troca de senha, etc.
    path('accounts/', include('django.contrib.auth.urls')), 
]
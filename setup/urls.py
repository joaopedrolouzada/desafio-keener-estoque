from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Rota do Painel Administrativo
    path('admin/', admin.site.urls),
    
    # 2. Rota do seu app de estoque
    path('estoque/', include('produtos.urls')), 
    
    # 3. Rota automática do Django para Login e Logout
    path('accounts/', include('django.contrib.auth.urls')), 
]
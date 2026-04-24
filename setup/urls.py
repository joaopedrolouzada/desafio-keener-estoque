from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [

    # 1. Rota do Painel Administrativo
    path('admin/', admin.site.urls),
    
    # 2. Rota do seu app de estoque
    path('estoque/', include('produtos.urls')), 
    
    # 3. Rota automática do Django para Login e Logout
    path('accounts/', include('django.contrib.auth.urls')), 

    # 4. Redireciona a página vazia para o estoque

    path('', lambda request: redirect('estoque/', permanent=False)),
]
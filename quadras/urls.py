from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Página inicial
    path('adicionar_quadra/', views.adicionar_quadra, name='adicionar_quadra'),
    path('sucesso/', views.sucesso, name='sucesso'),  # Configuração para a URL 'sucesso'
    path('quadra/<int:id>/', views.detalhes_quadra, name='detalhes_quadra'),  # URL dinâmica

]
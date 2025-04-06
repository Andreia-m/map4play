from django.shortcuts import render
from .models import Quadra  # Importe o modelo Quadra
from django.db.models import Q

def home(request):
    # Obter o valor da pesquisa (campo "q")
    query = request.GET.get('q', '')  # Captura o valor do campo "q" no formulário (ou vazio se não houver valor)

    # Filtro inicial: Retorna todas as quadras se não houver busca
    if query:
        # Filtrar quadras por nome ou endereço (pesquisa case-insensitive)
        quadras = Quadra.objects.filter(
            Q(nome__icontains=query) | Q(endereco__icontains=query)
        )
    else:
        quadras = Quadra.objects.all()  # Retorna todas as quadras

    # Passar as quadras para o template
    return render(request, 'quadras/home.html', {'quadras': quadras, 'query': query})

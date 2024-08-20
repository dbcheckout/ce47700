
# candidato/views.py
from django.shortcuts import render
from .models import PlanoGoverno, AcoesRealizadas


def landing_page(request):
    plano_governo = PlanoGoverno.objects.all()
    acoes_realizadas = AcoesRealizadas.objects.all().order_by('-data')
    return render(request, 'template/landing_page.html', {
        'plano_governo': plano_governo,
        'acoes_realizadas': acoes_realizadas,
    })
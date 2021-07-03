from django.shortcuts import render
from django.http import HttpResponse
from ..models import *

def index(request):
    contas_pagar = ContaPagar.objects.all()
    contas_receber = ContaReceber.objects.all()
    data = {
        'contas_pagar': contas_pagar,
        'contas_receber': contas_receber,
    }
    return render(request, 'index.html', data)

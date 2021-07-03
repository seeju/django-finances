from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from ..models import *

@csrf_exempt
def contas_receber_index(request):
    try:
        if request.method == 'GET':
            return contas_receber_obtain_all(request)
        elif request.method == 'POST':
            return contas_receber_insert(request)
        else:
            return JsonResponse(status=405)
    except Exception as e:
        return JsonResponse(str(e), status=500)

@csrf_exempt
def contas_receber_index_id(request, id):
    try:
        if request.method == 'GET':
            return contas_receber_obtain_id(request, id)
        elif request.method == 'PUT':
            return contas_receber_update(request, id)
        elif request.method == 'DELETE':
            return contas_receber_delete(request, id)
        else:
            return JsonResponse(status=405)
    except Exception as e:
        return JsonResponse(str(e), status=500)

def contas_receber_obtain_all(request):
    contas_receber = ContaReceber.objects.all()
    resposta = { 'contas_receber': list(map(lambda c: c.json(), contas_receber)) }
    return JsonResponse(resposta, status=200)

def contas_receber_insert(request):
    try:
        if not request.body:
            return JsonResponse({ 'mensagem': 'Requisicao nula' }, status=400)
        body = json.loads(request.body)
        if not 'classificacao' in body \
            or not 'valor' in body \
            or not 'descricao' in body \
            or not 'data_expectativa' in body \
            or not 'data_recebimento' in body \
            or not 'forma_pagamento' in body \
            or not 'classificacao' in body \
            or not 'situacao' in body:
            return JsonResponse({ 'mensagem': 'Campos nao preenchidos' }, status=400)

        forma_pagamento_obj = FormaPagamento.objects.get(descricao=body['forma_pagamento'])
        classificacao_obj = Classificacao.objects.get(descricao=body['classificacao'])

        conta_receber = ContaReceber()
        conta_receber.valor = body['valor']
        conta_receber.descricao = body['descricao']
        conta_receber.data_expectativa = body['data_expectativa']
        conta_receber.data_recebimento = body['data_recebimento']
        conta_receber.forma_pagamento = forma_pagamento_obj
        conta_receber.classificacao = classificacao_obj
        conta_receber.situacao = body['situacao']
        conta_receber.save()

        return HttpResponse(status=201)
    except FormaPagamento.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Forma de pagamento nao encontrada' }, status=400)
    except Classificacao.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Classificao nao encontrada' }, status=400)

def contas_receber_obtain_id(request, id):
    try:
        conta_receber = ContaReceber.objects.get(id=id)
        resposta = conta_receber.json()
        return JsonResponse(resposta, status=200)
    except ContaReceber.DoesNotExist:
        return HttpResponse(status=404)

def contas_receber_update(request, id):
    try:
        if not request.body:
            return JsonResponse({ 'mensagem': 'Requisicao nula' }, status=400)
        body = json.loads(request.body)
        if not 'classificacao' in body \
            or not 'valor' in body \
            or not 'descricao' in body \
            or not 'data_expectativa' in body \
            or not 'data_recebimento' in body \
            or not 'forma_pagamento' in body \
            or not 'classificacao' in body \
            or not 'situacao' in body:
            return JsonResponse({ 'mensagem': 'Campos nao preenchidos' }, status=400)

        conta_receber = ContaReceber.objects.get(id=id)
        forma_pagamento_obj = FormaPagamento.objects.get(descricao=body['forma_pagamento'])
        classificacao_obj = Classificacao.objects.get(descricao=body['classificacao'])

        conta_receber.valor = body['valor']
        conta_receber.descricao = body['descricao']
        conta_receber.data_expectativa = body['data_expectativa']
        conta_receber.data_recebimento = body['data_recebimento']
        conta_receber.forma_pagamento = forma_pagamento_obj
        conta_receber.classificacao = classificacao_obj
        conta_receber.situacao = body['situacao']
        conta_receber.save()

        return HttpResponse(status=202)
    except FormaPagamento.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Forma de pagamento nao encontrada' }, status=400)
    except Classificacao.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Classificao nao encontrada' }, status=400)
    except ContaReceber.DoesNotExist:
        return HttpResponse(status=404)

def contas_receber_delete(request, id):
    try:
        conta_receber = ContaReceber.objects.get(id=id)
        conta_receber.delete()
        return HttpResponse(status=200)
    except ContaReceber.DoesNotExist:
        return HttpResponse(status=404)

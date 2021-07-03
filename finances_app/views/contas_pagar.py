from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from ..models import *

@csrf_exempt
def contas_pagar_index(request):
    try:
        if request.method == 'GET':
            return contas_pagar_obtain_all(request)
        elif request.method == 'POST':
            return contas_pagar_insert(request)
        else:
            return HttpResponse(status=405)
    except Exception as e:
        return HttpResponse(status=500)

@csrf_exempt
def contas_pagar_index_id(request, id):
    try:
        if request.method == 'GET':
            return contas_pagar_obtain_id(request, id)
        elif request.method == 'PUT':
            return contas_pagar_update(request, id)
        elif request.method == 'DELETE':
            return contas_pagar_delete(request, id)
        else:
            return HttpResponse(status=405)
    except Exception as e:
        return HttpResponse(status=500)

def contas_pagar_obtain_all(request):
    contas_pagar = ContaPagar.objects.all()
    resposta = { 'contas_pagar': list(map(lambda c: c.json(), contas_pagar)) }
    return JsonResponse(resposta, status=200)

def contas_pagar_insert(request):
    try:
        if not request.body:
            return JsonResponse({ 'mensagem': 'Requisicao nula' }, status=400)
        body = json.loads(request.body)
        if not 'classificacao' in body \
            or not 'valor' in body \
            or not 'descricao' in body \
            or not 'data_vencimento' in body \
            or not 'data_pagamento' in body \
            or not 'forma_pagamento' in body \
            or not 'classificacao' in body \
            or not 'situacao' in body:
            return JsonResponse({ 'mensagem': 'Campos nao preenchidos' }, status=400)

        forma_pagamento_obj = FormaPagamento.objects.get(descricao=body['forma_pagamento'])
        classificacao_obj = Classificacao.objects.get(descricao=body['classificacao'])

        conta_pagar = ContaPagar()
        conta_pagar.valor = body['valor']
        conta_pagar.descricao = body['descricao']
        conta_pagar.data_vencimento = body['data_vencimento']
        conta_pagar.data_pagamento = body['data_pagamento']
        conta_pagar.forma_pagamento = forma_pagamento_obj
        conta_pagar.classificacao = classificacao_obj
        conta_pagar.situacao = body['situacao']
        conta_pagar.save()

        return HttpResponse(status=201)
    except FormaPagamento.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Forma de pagamento nao encontrada' }, status=400)
    except Classificacao.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Classificao nao encontrada' }, status=400)

def contas_pagar_obtain_id(request, id):
    try:
        conta_pagar = ContaPagar.objects.get(id=id)
        resposta = conta_pagar.json()
        return JsonResponse(resposta, status=200)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)

def contas_pagar_update(request, id):
    try:
        if not request.body:
            return JsonResponse({ 'mensagem': 'Requisicao nula' }, status=400)
        body = json.loads(request.body)
        if not 'classificacao' in body \
            or not 'valor' in body \
            or not 'descricao' in body \
            or not 'data_vencimento' in body \
            or not 'data_pagamento' in body \
            or not 'forma_pagamento' in body \
            or not 'classificacao' in body \
            or not 'situacao' in body:
            return JsonResponse({ 'mensagem': 'Campos nao preenchidos' }, status=400)

        conta_pagar = ContaPagar.objects.get(id=id)
        forma_pagamento_obj = FormaPagamento.objects.get(descricao=body['forma_pagamento'])
        classificacao_obj = Classificacao.objects.get(descricao=body['classificacao'])

        conta_pagar.valor = body['valor']
        conta_pagar.descricao = body['descricao']
        conta_pagar.data_vencimento = body['data_vencimento']
        conta_pagar.data_pagamento = body['data_pagamento']
        conta_pagar.forma_pagamento = forma_pagamento_obj
        conta_pagar.classificacao = classificacao_obj
        conta_pagar.situacao = body['situacao']
        conta_pagar.save()

        return HttpResponse(status=202)
    except FormaPagamento.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Forma de pagamento nao encontrada' }, status=400)
    except Classificacao.DoesNotExist:
        return JsonResponse({ 'mensagem': 'Classificao nao encontrada' }, status=400)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)

def contas_pagar_delete(request, id):
    try:
        conta_pagar = ContaPagar.objects.get(id=id)
        conta_pagar.delete()
        return HttpResponse(status=200)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)

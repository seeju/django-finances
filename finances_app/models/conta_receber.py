from django.db import models
from .classificacao import *
from .forma_pagamento import *

class ContaReceber(models.Model):
    SITUACAO = [
        (0, 'A Receber'),
        (1, 'Recebido'),
    ]

    valor = models.FloatField()
    descricao = models.CharField(max_length=60)
    data_expectativa = models.DateField()
    data_recebimento = models.DateField(default=None, blank=True, null=True)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    situacao = models.IntegerField(choices=SITUACAO)

    def __str__(self):
        self.option = {
            0: 'A Receber',
            1: 'Recebido',
        }[self.situacao]
        return '{self.descricao} ({self.option})'.format(self=self)

    def json(self):
        self.option = {
            0: 'A Receber',
            1: 'Recebido',
        }[self.situacao]
        return {
            'id': self.id,
            'valor': self.valor,
            'descricao': self.descricao,
            'data_expectativa': self.data_expectativa,
            'data_recebimento': self.data_recebimento,
            'forma_pagamento': self.forma_pagamento.descricao,
            'classificacao': self.classificacao.descricao,
            'situacao': self.option,
        }

    class Meta:
        verbose_name_plural = 'Contas a Receber'
        ordering = ['data_expectativa']

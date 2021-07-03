from django.db import models

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=60)

    def __str__(self):
        return '{self.descricao}'.format(self=self)

    class Meta:
        verbose_name_plural = "Formas de Pagamento"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contas_pagar', views.contas_pagar_index, name='contas_pagar'),
    path('contas_pagar/<int:id>', views.contas_pagar_index_id, name='contas_pagar'),
    path('contas_receber', views.contas_receber_index, name='contas_receber'),
    path('contas_receber/<int:id>', views.contas_receber_index_id, name='contas_receber'),
]

from django.conf.urls import url
from sitefazentech.views import *

urlpatterns = [

    url('funcionario/', FuncionarioView.as_view(),name='funcionario'),
    url('controledeplantio/', ControleDePlantioView.as_view(),name='plantio'),
    url('controledeanimal/', ControleDeAnimalView.as_view(),name='animal'),
    url('varegista/', VaregistaView.as_view(),name='varegista'),
    url('equipamento/', EquipamentoView.as_view(),name='equipamento'),
    url('producaodeleite/', ProducaoDeLeiteView.as_view(),name='producaodeleite'),
    url('tipodeproducao/', ProducaoView.as_view(),name='tipodeproducao'),
    url('buscabinaria/', BuscaBinariaView.as_view(),name='buscabinaria'),
    url('lista/', ListaView.as_view(),name='lista'),
    url('atualizar/(?P<pk>\d+)', UpdateDeleteView.as_view(),name='atualizar'),
url('delete/(?P<pk>\d+)', DeleteView.as_view(),name='delete'),
    url(r'', TesteView.as_view()),


]
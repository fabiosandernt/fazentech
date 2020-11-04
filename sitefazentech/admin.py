from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Setor)
admin.site.register(Funcionario)
admin.site.register(EspecieDeVaca)
admin.site.register(TipoEstabelecimento)
admin.site.register(Varegista)
admin.site.register(TipoEquipamento)
admin.site.register(Equipamento)
admin.site.register(ProducaoDeLeite)
admin.site.register(TipoDeProducao)
admin.site.register(ControleDePlantio)
admin.site.register(ControleDeAnimal)
admin.site.register(Producao)


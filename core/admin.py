from django.contrib import admin
from .models import Cargo, Equipe, Servico
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo','modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo','modificado')


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'cargo', 'ativo','modificado')

from django.http import HttpResponse
from django.contrib import admin
from .models import CampanhaEleitoral,LocalArmazenamento,MaterialCampanha,Estoque,MovimentacaoMaterial,Equipe,Municipio,Regiao,Bairro,AtividadeCampanha,AplicacaoMaterial,PlanoDeGoverno, Proposta, Acao

# Register your models here.

admin.site.register(PlanoDeGoverno)
admin.site.register(Proposta)
admin.site.register(Acao)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
 list_display = ('nome','funcao')
 search_fields = ('nome',)
 list_filter = ('nome',)

@admin.register(CampanhaEleitoral)
class CampanhaEleitoralAdmin(admin.ModelAdmin):
 list_display = ('nome', 'ativo', 'nome_registro','candidato','numero')
 search_fields = ('nome',)
 list_filter = ('nome',)

@admin.register(LocalArmazenamento)
class LocalArmazenamentoAdmin(admin.ModelAdmin):
 list_display = ('nome',)
 search_fields = ('nome',)
 list_filter = ('nome',)

@admin.register(MaterialCampanha)
class MaterialCampanhaAdmin(admin.ModelAdmin):
 list_display = ('nome',)
 search_fields = ('nome',)
 list_filter = ('nome',)

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
 list_display = ('material',)
 search_fields = ('material',)
 list_filter = ('material',)

@admin.register(MovimentacaoMaterial)
class MovimentacaoMaterialAdmin(admin.ModelAdmin):
 list_display = ('material','local_destino','quantidade','data_movimentacao')
 search_fields = ('material',)
 list_filter = ('material',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
 list_display = ('nome','estado')
 search_fields = ('nome',)
 list_filter = ('nome',)


@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
 list_display = ('nome','municipio','regional','populacao')
 search_fields = ('nome',)
 list_filter = ('nome',)


@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
 list_display = ('nome','municipio','regiao','populacao',)
 search_fields = ('nome',)
 list_filter = ('nome',)

@admin.register(AtividadeCampanha)
class AtividadeCampanhaAdmin(admin.ModelAdmin):
 list_display = ('tipo','regiao','bairro','data_hora',)
 search_fields = ('tipo','regiao',)
 list_filter = ('tipo','regiao',)

@admin.register(AplicacaoMaterial)
class AplicacaoMaterialAdmin(admin.ModelAdmin):
 list_display = ('material','local_aplicacao','quantidade','descricao',)
 search_fields = ('material','local_aplicacao','quantidade','descricao',)
 list_filter = ('material','local_aplicacao','quantidade','descricao',)






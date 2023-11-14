from django.contrib import admin
from .models import *
from .forms import MembroForm, FuncaoForm, PequenoGrupoForm

class FuncaoInline(admin.TabularInline):
    model = Funcao.membroFuncao.through
    form = FuncaoForm
    extra = 1

class PequenoGrupoInline(admin.TabularInline):
    model = PequenoGrupo.membrosPequenoGrupo.through
    form = PequenoGrupoForm
    extra = 1

class MembroAdmin(admin.ModelAdmin):
    inlines = [FuncaoInline, PequenoGrupoInline]
    form = MembroForm

admin.site.register(Membro, MembroAdmin)
admin.site.register(Visita)
admin.site.register(Ministerio)
admin.site.register(TipoInstrumento)
admin.site.register(Instrumento)
admin.site.register(Funcao)
admin.site.register(PequenoGrupo)
admin.site.register(Evento)

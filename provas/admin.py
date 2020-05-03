from django.contrib import admin
from .models import Cliente, Parceirias, duvidas


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Cliente,ClienteAdmin)

class ParceiriasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'proposta')

admin.site.register(Parceirias,ParceiriasAdmin)

class duvidasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'duvidas')

admin.site.register(duvidas,duvidasAdmin)
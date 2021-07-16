from django.contrib import admin

from api import models


@admin.register(models.Conexao)
class ConexaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'email']

@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['data', 'de', 'para', 'assunto']

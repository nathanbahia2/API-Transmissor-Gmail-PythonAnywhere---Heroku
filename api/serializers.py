from rest_framework import serializers

from api import models


class ConexaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conexao
        fields = ['descricao', 'email']        


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ['data', 'de', 'para', 'assunto', 'mensagem']

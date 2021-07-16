from rest_framework import serializers

from api import models


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ['id', 'data', 'de', 'para', 'assunto', 'mensagem']

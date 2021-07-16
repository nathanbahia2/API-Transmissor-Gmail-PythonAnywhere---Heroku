from django.db import models


class Conexao(models.Model):
    descricao = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Email(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    de = models.ForeignKey(Conexao, on_delete=models.SET_NULL, null=True, related_name='emails_enviados')
    para = models.TextField()
    assunto = models.TextField(blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.assunto

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from api import serializers, models


class EmailViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        obj = generics.get_object_or_404(
            models.Conexao, 
            pk=serializer.data['de']
        )

        email = obj.email
        senha = obj.senha
        para = serializer.data['para'].split(',')
        assunto = serializer.data['assunto']
        mensagem = serializer.data['mensagem']

        settings.EMAIL_HOST_USER = email
        settings.EMAIL_HOST_PASSWORD = senha

        msg = EmailMultiAlternatives(
            subject=assunto,
            body=mensagem,
            from_email=settings.EMAIL_HOST_USER,
            to=para
        )
        msg.attach_alternative(mensagem, "text/html")
        msg.send()

        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers)

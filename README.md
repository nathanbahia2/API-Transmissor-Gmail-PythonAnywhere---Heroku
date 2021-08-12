# API Transmissor G-mail PythonAnywhere-Heroku

##### API desenvolvida para sanar a necessidade de enviar e-mails por aplicações hospedas no Heroku utilizando um servidor de e-mails seguro e gratuito (G-mail).
##### Por motivos de segurança, o G-mail não permite envios de e-mails por aplicações hospedadas no Heroku, por outro lado, no PythonAnywhere é possível. Pensando nisso, desenvolvi esta API que está hospedada gratuitamente no [PythonAnywhere](https://pythonanywhere.com) para que seja possível realizar requisições para o endpoit designidado a enviar os e-mails e realizar a gravação dos logs de envio.

##### Atualmente, esta API está sendo consumida pelo [Sistema de Comunicação Interna](https://github.com/nathanbahia2/Comunicacao-Interna) que desenvolvi para uma empresa na qual já trabalhei. Porém, para os próximos projetos que eu desenvolver, está API irá suprimir minhas necessidadesde envios de e-mails.


Para testar o projeto em sua máquina, siga os seguintes passos:

```
# Criação do ambiente virtual
python -m venv venv


# Ativação do ambiente virtual

- Windows
venv\script\activate

- Linux e MAC-OS
source venv\bin\activate


# Instalação dos pacotes
pip install -r requirements.txt


# Aplicação das migrações do banco de dados
python manage.py migrate


# Criação de um superusuário
python manage.py createsuperuser


# Execução do servidor local
python manage.py runserver 
```

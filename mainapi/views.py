from rest_framework import viewsets
from .models import *
from .serializers import *


class AboutUsViewset(viewsets.ModelViewSet):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()


class ServicesViewset(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()


class AnnouncementsViewset(viewsets.ModelViewSet):
    serializer_class = AnnouncementsSerializer
    queryset = Announcements.objects.all()


class ContactsViewset(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class RequisitesViewset(viewsets.ModelViewSet):
    serializer_class = RequisitesSerializer
    queryset = Requisites.objects.all()
    

class HistoryViewset(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()


class HerosViewset(viewsets.ModelViewSet):
    serializer_class = HerosSerializer
    queryset = Heros.objects.all()


class AboutUsMoreViewset(viewsets.ModelViewSet):
    serializer_class = AboutUsMoreSerializer
    queryset = AboutUsMore.objects.all()


# from django.core.mail import send_mail
# import smtplib
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def SendEmailViewset(request):

#     if request.method == 'GET':
#         model = SendEmailModel.objects.all()
#         serializer = SendEmailSerailizer(model, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SendEmailSerailizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# class SendEmailViewset(viewsets.ModelViewSet):
#     serializer_class =  SendEmailSerailizer
#     queryset = SendEmailModel.objects.all()

#     email = SendEmailModel.objects.last()

#     # send_mail(
#     #     'SUBJECT', 'Message', 
#     #     'abdunazarovdior@mail.ru',
#     #     ['something@gmail.com',], 
#     #     fail_silently=False
#     #     )

#     # if request.method == 'POST':
#     #     print('GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!')

#     @action(detail=True, methods=['post'])
#     def post(self, request):
#         print('GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!')

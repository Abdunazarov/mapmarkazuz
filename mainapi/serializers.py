from re import search
from turtle import ondrag
from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'



class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'  


class RequisitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisites
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__' 


class HerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heros
        fields = '__all__' 


class AboutUsMoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsMore
        fields = '__all__' 


# class SendEmailSerailizer(serializers.ModelSerializer):
#     class Meta:
#         model = SendEmailModel
#         fields = '__all__'
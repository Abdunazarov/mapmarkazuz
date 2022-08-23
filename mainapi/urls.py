import imp
from stringprep import b1_set
from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('AboutUs', AboutUsViewset)
router.register('Services', ServicesViewset)
router.register('Announcements', AnnouncementsViewset)
router.register('Contacts', ContactsViewset)
router.register('Requisites', RequisitesViewset)
router.register('History', HistoryViewset)
router.register('Heros', HerosViewset)
router.register('AboutUsMore', AboutUsMoreViewset)
# router.register('SendEmail', SendEmailViewset, basename='sendemail')




urlpatterns = [
    path('', include(router.urls)),
    path('SendEmail/', SendEmailViewset)
]


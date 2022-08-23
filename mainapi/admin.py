from atexit import register
from optparse import AmbiguousOptionError
from django.contrib import admin
from .models import *


admin.site.register(AboutUs)
admin.site.register(Services)
admin.site.register(Contacts)
admin.site.register(Requisites)
admin.site.register(Announcements)
admin.site.register(History)
admin.site.register(AboutUsImg)
admin.site.register(Heros)
admin.site.register(AboutUsMore)
admin.site.register(images)
admin.site.register(SendEmailModel)
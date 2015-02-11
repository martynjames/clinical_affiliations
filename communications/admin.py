""" models to expose to the admin user interface """
from django.contrib import admin
from communications.models import Institution, Contact, Communication

# Register your models here.
admin.site.register(Institution)
admin.site.register(Contact)
admin.site.register(Communication)

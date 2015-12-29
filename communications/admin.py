""" models to expose to the admin user interface """
from django.contrib import admin
from communications.models import Institution, Contact, Communication, Rotation, Housing, Payment

# Register your models here.
admin.site.register(Institution)
admin.site.register(Contact)
admin.site.register(Communication)
admin.site.register(Rotation)
admin.site.register(Housing)
admin.site.register(Payment)

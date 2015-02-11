""" Models for relationships between Institutions, Contacts and Communications """
from django.db import models

# Models


class Institution(models.Model):
    """ A model representing an Institution with which one has communications with one or more contacts """
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    """ A model representing the people with whom communications are being performed """
    institution = models.ForeignKey(Institution)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    appointment_status = models.CharField(max_length=100)
    number_of_students = models.IntegerField()
    details = models.TextField()
    active_since = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Communication(models.Model):
    """ A model representing an individual communication item with a specific contact """
    contact = models.ForeignKey(Contact)
    timestamp = models.DateTimeField('communication date')
    details = models.TextField()

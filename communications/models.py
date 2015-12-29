""" Models for relationships between Institutions, Contacts and Communications """
from django.db import models

# Models


class Institution(models.Model):
    """ A model representing an Institution with which one has communications with one or more contacts """
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    major_affiliate = models.BooleanField(default=False)
    agreement_date = models.DateField(blank=True, null=True)

    bed_count = models.IntegerField(blank=True, null=True)
    occupancy_rate = models.IntegerField(blank=True, null=True)
    average_stay = models.IntegerField(blank=True, null=True)

    # per-year data points
    annual_admissions = models.IntegerField(blank=True, null=True)
    annual_outpatient_visits = models.IntegerField(blank=True, null=True)
    annual_emergency_visits = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Rotation(models.Model):
    """ A model representing a rotation at an institution """
    ROTATION_TYPE_CHOICES = (
        ("MED", "Medicine"),
        ("SURG", "Surgery"),
        ("PEDS", "Pediatrics"),
        ("FAM", "Family Medicine"),
        ("OBGN", "OB/GYN"),
        ("PSYC", "Psychiatry"),
        ("NEUR", "Neurology"),
        ("RADI", "Radiology"),
        ("PA", "PA"),
        ("ELEC", "Elective"),
    )
    institution = models.ForeignKey(Institution)
    rotation_type = models.CharField(max_length=4, choices=ROTATION_TYPE_CHOICES, default=None)
    number_of_students = models.IntegerField()
    annual_number_of_rotations = models.IntegerField()
    details = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{} rotation at {}".format(self.rotation_type, unicode(self.institution))


class InstitutionUniqueBooleanField(models.BooleanField):

    def pre_save(self, model_instance, add):
        filter_kwargs = {
            "institution": model_instance.institution,
            self.attname: True,
        }
        exclude_kwargs = {
            "id": model_instance.id
        }
        contacts = model_instance.__class__.objects.filter(**filter_kwargs).exclude(**exclude_kwargs)

        # If True then set all others as False
        if getattr(model_instance, self.attname):
            contacts.update(**{self.attname: False})

        return getattr(model_instance, self.attname)


class Contact(models.Model):
    """ A model representing the people with whom communications are being performed """
    institution = models.ForeignKey(Institution, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    appointment_status = models.CharField(max_length=100, blank=True, null=True)
    number_of_students = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    active_since = models.CharField(max_length=100, blank=True, null=True)

    # Special contact flags
    ceo = InstitutionUniqueBooleanField(default=False)
    primary_contact = InstitutionUniqueBooleanField(default=False)
    administrative_contact = InstitutionUniqueBooleanField(default=False)

    # Faculty specific fields
    faculty_for_rotation = models.ForeignKey(Rotation, blank=True, null=True)
    buid_form_submitted = models.DateField(blank=True, null=True)
    appointment_packet_submitted = models.DateField(blank=True, null=True)
    appointment_finalized = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)


class Housing(models.Model):
    """ A location in which to house students """
    institution = models.ForeignKey(Institution)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    beds = models.IntegerField()
    singles = models.IntegerField(blank=True, null=True)
    shared = models.IntegerField(blank=True, null=True)
    rotation_info = models.TextField(blank=True, null=True)
    housing_contact = models.OneToOneField(Contact, blank=True, null=True)

    def __unicode__(self):
        return u"Housing at {}, {} for {}".format(self.address_1, self.city, institution)


class Payment(models.Model):
    """ A payment made to an institution """
    institution = models.ForeignKey(Institution)
    date = models.DateField()
    amount = models.IntegerField()
    paid_to = models.CharField(max_length=1024)

    def __unicode__(self):
        return u"Payment for {} on {}".format(self.institution, date)


class Communication(models.Model):
    """ A model representing an individual communication item with a specific contact """
    contact = models.ForeignKey(Contact)
    datestamp = models.DateField('communication date')
    details = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Communication with {} on {}".format(self.contact, datestamp)

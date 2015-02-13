""" Views for communications endpoints """
from django.shortcuts import render

from .models import Institution, Contact, Communication

# Create your views here.


def institutions(request):
    """ List the institutions with which we are affiliated """
    data = {
        "institutions": Institution.objects.all(),
    }
    return render(request, 'communications/institutions.haml', data)


def institution(request, institution_id):
    """ Detail view for specific institution """
    the_institution = Institution.objects.get(pk=institution_id)
    institution_contacts = Contact.objects.filter(institution=the_institution)
    for institution_contact in institution_contacts:
        communications = Communication.objects.filter(contact=institution_contact)
        institution_contact.latest_communication = communications[0].datestamp if len(communications) else None
    data = {
        "institution": the_institution,
        "contacts": institution_contacts
    }
    return render(request, 'communications/institution.haml', data)


def contact(request, contact_id):
    """ Detail view for specific contact """
    the_contact = Contact.objects.get(pk=contact_id)
    data = {
        "contact": the_contact,
        "communications": Communication.objects.filter(contact=the_contact)
    }
    return render(request, 'communications/contact.haml', data)

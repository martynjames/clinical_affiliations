""" Views for communications endpoints """
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Institution, Contact, Communication
from .forms import InstitutionForm, ContactForm, CommunicationForm

# Create your views here.


@login_required
def institutions(request):
    """ List the institutions with which we are affiliated """
    if request.method == "POST":
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "please fix the problems indicated below."

    data = {
        "institutions": Institution.objects.all().order_by('name'),
        "form": InstitutionForm()
    }
    return render(request, 'communications/institutions.haml', data)


@login_required
def institution(request, institution_id):
    """ Detail view for specific institution """
    the_institution = Institution.objects.get(pk=institution_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "please fix the problems indicated below."

    institution_contacts = Contact.objects.filter(institution=the_institution).order_by('last_name')
    for institution_contact in institution_contacts:
        communications = Communication.objects.filter(contact=institution_contact).order_by('-datestamp')
        institution_contact.latest_communication = None
        if len(communications):
            institution_contact.latest_communication = "{} | {}".format(
                communications[0].datestamp,
                communications[0].details[:100],
            )
    data = {
        "institution": the_institution,
        "contacts": institution_contacts,
        "form": ContactForm({"institution": institution_id}),
    }
    return render(request, 'communications/institution.haml', data)


@login_required
def contact(request, contact_id):
    """ Detail view for specific contact """
    the_contact = Contact.objects.get(pk=contact_id)
    if request.method == "POST":
        form = CommunicationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "please fix the problems indicated below."

    data = {
        "contact": the_contact,
        "communications": Communication.objects.filter(contact=the_contact).order_by('-created'),
        "form": CommunicationForm({"contact": contact_id, "datestamp": datetime.now()})
    }
    return render(request, 'communications/contact.haml', data)

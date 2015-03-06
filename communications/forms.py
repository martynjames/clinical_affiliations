from django import forms

from .models import Institution, Contact, Communication


class InstitutionForm(forms.ModelForm):
    ''' add a new institution '''
    class Meta:
        model = Institution
        exclude = []


class ContactForm(forms.ModelForm):
    ''' add a new contact '''
    class Meta:
        model = Contact
        exclude = []


class CommunicationForm(forms.ModelForm):
    ''' add a new contact '''
    class Meta:
        model = Communication
        exclude = []

from django import forms

class AddWorkerForm(forms.Form):
    full_name = forms.CharField(label='full_name', max_length=200)
    passport_number = forms.CharField(label='passport_number', max_length=200)
    workers_contacts = forms.CharField(label='workers_contacts', max_length=200)

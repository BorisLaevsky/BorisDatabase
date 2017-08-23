from django import forms


class AddWorkerForm(forms.Form):
    full_name = forms.CharField(label='full_name', max_length=200)
    passport_number = forms.CharField(label='passport_number', max_length=200)
    workers_contacts = forms.CharField(label='workers_contacts', max_length=200)


class SearchWorkerForm(forms.Form):
    passport_number = forms.CharField(label='passport_number', max_length=200)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)


class AddCompanyForm(forms.Form):
    company_name = forms.CharField(label='company_name', max_length=200)
    company_contact = forms.CharField(label='company_contact', max_length=200)
    company_adress = forms.CharField(label='company_adress', max_length=200)

class SearchCompanyForm(forms.Form):
    company_name = forms.CharField(label='company_name', max_length=200)



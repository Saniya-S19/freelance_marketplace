from django import forms
from . models import FreelancerProfile, ClientProfile

class FreelancerProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        fields = '__all__'
        exclude = ['user']

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        exclude = ['user']

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),
            'company_desc': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell freelancers about your company'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, State'
            }),
        }
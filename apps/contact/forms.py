from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'subject': forms.TextInput(attrs={'required': True}),
            'message': forms.Textarea(attrs={'required': True}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email é obrigatório.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        for field in ['name', 'email', 'subject', 'message']:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo é obrigatório.')
        return cleaned_data

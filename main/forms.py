from django import forms

from my_resume import settings
from . models import ContactProfile


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'class': 'form-control',
			'rows': 6,
			}))
	recipient_list = [settings.EMAIL_HOST_USER, 'recipient@example.com']

	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
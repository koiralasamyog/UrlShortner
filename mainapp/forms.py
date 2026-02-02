# mainapp/forms.py
from django import forms
from .models import ShortURL

class CreateNewShortURL(forms.ModelForm):
    custom_short_url = forms.CharField(
        max_length=10, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Custom short URL (optional)'})
    )
    expiration_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = ShortURL
        fields = ['original_url', 'custom_short_url', 'expiration_date']
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter the long URL'})
        }

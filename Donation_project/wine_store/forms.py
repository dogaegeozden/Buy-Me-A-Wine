# LIBRARIES
from django import forms

# MODELS
from .models import (
    Message,
)



# FORM CLASSES

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'full_name',
            'email',
            'message',
        ]

    full_name = forms.CharField(max_length=70, label="Name")
    email = forms.CharField(max_length=120, label="E-mail")
    message = forms.CharField(max_length=10000, label="Message")


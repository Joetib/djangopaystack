from django import forms
from . import models

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ('amount', 'email')
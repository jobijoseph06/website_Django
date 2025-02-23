from django import forms
from .models import Form  # Import your model

class ApplicationForm(forms.ModelForm):  # ✅ Use ModelForm
    class Meta:
        model = Form
        fields = ['first_name', 'last_name', 'email', 'date', 'occupation', 'resume']

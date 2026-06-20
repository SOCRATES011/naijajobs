from django import forms
from .models import Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','company','location','job_type','salary_min','salary_max','description','category','is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows':6}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

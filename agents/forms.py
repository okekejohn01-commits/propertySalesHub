from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class AgentSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True, label="WhatsApp Number")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']


class AgentProfileForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True, label="WhatsApp Number")
    new_password = forms.CharField(
        required=False,
        label="New password",
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        required=False,
        label="Confirm new password",
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, user, profile=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.profile = profile
        self.fields['email'].initial = user.email
        self.fields['phone'].initial = profile.phone if profile else ''

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password or confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("The new passwords do not match.")
        return cleaned_data
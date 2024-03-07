import uuid

from django import forms


import settings.settings
from accounts.models import OnlineShopUser
from accounts.tasks import activate_email


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = OnlineShopUser
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password1"] != cleaned_data["password2"]:
            self.add_error("password2", "Password do not match")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.is_active = False
        instance.username = str(uuid.uuid4())
        instance.set_password(self.cleaned_data["password1"])

        from django.urls import reverse

        activate_email(
            # f'http://localhost:8000/{reverse("accounts:activate-user",instance.username)},
            f'{settings.settings.HTTP_SCHEMA}://{settings.settings.DOMAIN}/'
            f'activate/{instance.username}',
            instance.email
        )

        # print(f'http://localhost:8000/accounts/activate/{instance.username}/')

        if commit:
            instance.save()

        return instance




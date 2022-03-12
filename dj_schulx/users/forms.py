from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from .models import Guardian, Teacher, User

# from django.contrib.auth import get_user_model


# active_user = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class GuardianCreationForm(admin_forms.UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=9)

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        Guardian.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
        )
        return user


class TeacherCreationForm(admin_forms.UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=9)
    street = forms.CharField(max_length=255, required=False)
    postal_code = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=False)
    PESEL = forms.CharField(max_length=255, required=False)
    bank_account_number = forms.CharField(max_length=255, required=False)

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        Teacher.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
            street=self.cleaned_data["street"],
            postal_code=self.cleaned_data["postal_code"],
            city=self.cleaned_data["city"],
            PESEL=self.cleaned_data["PESEL"],
            bank_account_number=self.cleaned_data["bank_account_number"],
        )
        return user


# taki sam jak GuardianCreationForm tylko user_type = 3 - dziedziczyć?
class ManagerCreationForm(admin_forms.UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=9)

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 3
        user.save()
        Guardian.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
        )
        return user

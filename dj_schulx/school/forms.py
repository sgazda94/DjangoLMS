from django import forms
from django.contrib.auth import get_user_model

from dj_schulx.groups.models import Group
from dj_schulx.users.models import Student

User = get_user_model()


class AddStudentToGroupForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        pass

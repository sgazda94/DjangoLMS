from django import forms
from django.contrib.auth import get_user_model

from dj_schulx.users.models import Teacher

from .models import Group, Lesson

active_user = get_user_model()


class DateInput(forms.DateInput):
    input_type = "date"


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        if "user" in kwargs:
            user = kwargs.pop("user")
            super(GroupForm, self).__init__(*args, **kwargs)
            teacher = Teacher.objects.get(user=user)
            self.fields["teacher"].initial = teacher
        else:
            super(GroupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Group
        fields = ("course", "teacher", "week_day", "start_time", "end_time", "students")
        widgets = {
            "start_time": forms.TimeInput(attrs={"type": "time", "step": 300}),
            "end_time": forms.TimeInput(attrs={"type": "time", "step": 300}),
        }


class LessonForm(forms.ModelForm):
    class Meta:

        model = Lesson
        fields = ("teacher", "lesson_script", "date", "start_time", "end_time")
        widgets = {
            "date": DateInput(),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }


class StartLessonForm(forms.Form):
    pass

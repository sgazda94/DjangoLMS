from datetime import date

from django import forms

from dj_schulx.users.models import Teacher

from .models import Group, Lesson


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
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }


class LessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        if "user" in kwargs:
            user = kwargs.pop("user")
            group = kwargs.pop("group")
            group = Group.objects.get(id=group)
            super(LessonForm, self).__init__(*args, **kwargs)
            teacher = Teacher.objects.get(user=user)
            self.fields["teacher"].initial = teacher
            self.fields["start_time"].initial = group.start_time
            self.fields["end_time"].initial = group.end_time
            self.fields["date"].initial = date.today
        else:
            super(LessonForm, self).__init__(*args, **kwargs)

    class Meta:

        model = Lesson
        fields = ("teacher", "lesson_script", "date", "start_time", "end_time")
        widgets = {
            "date": DateInput(),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }

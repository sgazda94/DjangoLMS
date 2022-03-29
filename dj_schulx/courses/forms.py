from django import forms
from markdownx.fields import MarkdownxFormField

from dj_schulx.courses.models import LessonScript


class LessonScriptForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = LessonScript
        fields = "__all__"

from courses.models import LessonScript
from django import forms
from markdownx.fields import MarkdownxFormField


class LessonScriptForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = LessonScript
        fields = "__all__"


# class LessonUpdateForm(forms.Form):
#     bar = forms.CharField(widget=SummernoteInplaceWidget())

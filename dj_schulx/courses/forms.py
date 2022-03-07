from courses.models import LessonScript
from django import forms
from markdownx.fields import MarkdownxFormField


class LessonScriptForm(forms.ModelForm):
    class Meta:
        model = LessonScript
        fields = "__all__"
        widgets = {
            "content": MarkdownxFormField(),
        }


# class LessonUpdateForm(forms.Form):
#     bar = forms.CharField(widget=SummernoteInplaceWidget())

from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    post_text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'post_text',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        post_text = cleaned_data.get("post_text")

        if title == post_text:
            raise ValidationError(
                "The title does not have to be identical to the content."
            )

        return cleaned_data
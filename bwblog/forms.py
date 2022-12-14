from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ["body", 'parent']


class ContactForm(forms.Form):  # email contact form 
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_description(self):
        if not self.cleaned_data['name'].str.strip():
            raise forms.ValidationError('Enter a valid name!')



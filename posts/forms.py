from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    colors = (
        ('mysql', 'MySql'),
        ('sqlite', 'Sqlite'),
        ('mongo', 'MongoDb'),
    )
    bd = forms.ChoiceField(widget=forms.Select, choices=colors)

    class Meta:
        model = Posts
        fields = ('title', 'body')

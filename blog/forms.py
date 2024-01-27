from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    model = Blog
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

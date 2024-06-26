from blog_app.models import Blog
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control'}),
            'content': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends"),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('draft', 'Draft'), ('published', 'Published')]),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title is None or title.strip() == '':
            raise forms.ValidationError("The title cannot remain empty")
        
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if content is None or content.strip() == '':
            raise forms.ValidationError("The content cannot remain empty")
        
        return content

    def clean_status(self):
        status = self.cleaned_data.get('status')

        if status is None or status.strip() == '':
            raise forms.ValidationError("The title cannot remain empty")
        
        return status
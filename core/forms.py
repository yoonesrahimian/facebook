from django import forms
from core.models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'عنوان پستن'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'محتوای پست', 'row':'3', 'cols':'30'}))
#     user = forms.CharField()
#     subject = forms.CharField()

#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) < 3:
#             raise forms.ValidationError("عنوان نمی‌تواند کمتر از 3 کاراکتر باشد")
#         return title
    
#     def clean(self):
#         data = super().clean()
#         title = data.get('title')
#         content = data.get('content')
#         if not title in content:
#             raise forms.ValidationError("عنوان حتما باید داخل محتوا باشد")
#         return data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'user', 'subject', 'visible', 'is_deleted')
        widget = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'cols': 30, 'rows': 5, 'placeholder':'محتوا'}),
            'user': forms.Select(attrs={'class':'form-select'}),
            'subject': forms.Select(attrs={'class':'form-select'}),
            'visible': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

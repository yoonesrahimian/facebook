from django import forms

class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'عنوان پستن'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'محتوای پست', 'row':'3', 'cols':'30'}))
    user = forms.CharField()
    subject = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("عنوان نمی‌تواند کمتر از 3 کاراکتر باشد")
        return title
    
    def clean(self):
        data = super().clean()
        title = data.get('title')
        content = data.get('content')
        if not title in content:
            raise forms.ValidationError("عنوان حتما باید داخل محتوا باشد")
        return data
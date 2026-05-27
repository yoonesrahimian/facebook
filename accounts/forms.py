from django import forms
from accounts.models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'first_name', 'last_name', 'email',
        ]
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = CustomUser.objects.filter(username=username)
        if user:
            raise forms.ValidationError('کاربری با این نام کاربری قبلا ثبت نام کرده است.')
        return username

    def clean(self):
        data = super().clean()
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('گذرواژه مطابقت ندارد.')
        return data
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
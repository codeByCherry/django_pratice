from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='#用户名#')
    password = forms.CharField(label='#密码#', widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次确认', widget=forms.PasswordInput)

    # 指定相关的模型
    class Meta:
        model = User
        # 该form 需要对 username 和 email 赋值
        fields = ('username', 'email')

    # 校验password2 是否和 password 相等
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次密码不同!!')
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',
                  'birth',
                  )

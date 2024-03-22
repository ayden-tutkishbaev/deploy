from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm

from .models import Article, Profile


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'description',
                  'photo',
                  'category')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок статьи'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание статьи'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                               }))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'
                               }))


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                               }))

    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Ваше имя'
                                 }))
    last_name = forms.CharField(label="Ваша фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Ваша фамилия'
                                }))

    email = forms.EmailField(label="Ваша почта",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваша почта'
                             }))

    password1 = forms.CharField(label='Придумайте пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Придумайте пароль'
                                }))
    password2 = forms.CharField(label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Подтвердите пароль'
                                }))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                               }))

    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Ваше имя'
                                 }))
    last_name = forms.CharField(label="Ваша фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Ваша фамилия'
                                }))

    email = forms.EmailField(label="Ваша почта",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваша почта'
                             }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'phone',
            'mobile',
            'address',
            'job',
            'image'
        )

        widgets = {
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


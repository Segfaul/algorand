from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class ArraySearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    array = forms.CharField(label='Массив', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    target = forms.CharField(label='Искомое значение', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-input'}))

    def clean(self):
        try:
            cleaned_data = super().clean()
            array = list(map(float, cleaned_data.get('array').split(',')))
            target = float(cleaned_data.get('target'))

            if array != sorted(array):
                raise forms.ValidationError('Введенный массив должен быть отсортированным.')

            cleaned_data['array'] = array
            cleaned_data['target'] = target

        except Exception as error:
            raise forms.ValidationError(f"{error.__class__.__name__} {error.args[0]}")

        return cleaned_data


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


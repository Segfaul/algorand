import pandas as pd
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class ArraySearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    array = forms.CharField(label='Массив', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            required=False)
    target = forms.CharField(label='Искомое значение', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-input'}))
    file = forms.FileField(label='Загрузить отсортированный массив данных',
                           widget=forms.ClearableFileInput(attrs={'class': 'form-input', 'accept': '.xlsx,.csv,.txt'}),
                           required=False)

    def clean(self):
        try:
            cleaned_data = super().clean()
            target = float(cleaned_data.get('target'))
            array = list(map(float, cleaned_data.get('array').split(','))) if cleaned_data.get('array') else 0
            uploaded_file = cleaned_data.get('file')

            if array and array != sorted(array):
                raise forms.ValidationError('Введенный массив должен быть отсортированным.')

            if not array and not uploaded_file:
                raise forms.ValidationError('Пожалуйста, введите массив или загрузите файл.')

            if uploaded_file:
                file_extension = uploaded_file.name.split('.')[-1].lower()
                if file_extension not in ['csv', 'xlsx', 'txt']:
                    raise forms.ValidationError('Пожалуйста, загрузите файл в формате CSV, XLSX или TXT.')
                try:
                    if file_extension == 'csv':
                        array = self._read_csv_file(uploaded_file)
                    elif file_extension == 'xlsx':
                        array = self._read_excel_file(uploaded_file)
                    elif file_extension == 'txt':
                        array = self._read_text_file(uploaded_file)
                except Exception as error:
                    raise forms.ValidationError(f"Ошибка при чтении файла: {error}")

            cleaned_data['array'] = array
            cleaned_data['target'] = target

        except Exception as error:
            raise forms.ValidationError(f"{error.__class__.__name__} {error.args[0]}")

        return cleaned_data

    def _read_csv_file(self, uploaded_file):
        csv_file = pd.read_csv(uploaded_file)
        return csv_file.iloc[:, 0].tolist()

    def _read_excel_file(self, uploaded_file):
        excel_file = pd.read_excel(uploaded_file)
        return excel_file.iloc[:, 0].tolist()

    def _read_text_file(self, uploaded_file):
        lines = uploaded_file.readlines()
        return [float(line.strip()) for line in lines]


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


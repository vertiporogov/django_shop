from django import forms

from catalog.models import Product, Version



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        data_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if cleaned_data in data_list:
            raise forms.ValidationError('Такое название не подходит')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        data_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in data_list:
            if i in cleaned_data:
                raise forms.ValidationError('Такое описание не подходит')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_activ(self):
        cleaned_data = self.cleaned_data['is_activ']

        if cleaned_data:
            # Проверяем, существует ли активная версия в базе данных
            if Version.objects.filter(is_activ=True).exists():
                raise forms.ValidationError('Уже существует активная версия')

        return cleaned_data


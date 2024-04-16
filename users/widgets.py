from django import forms
from django.utils.translation import gettext_lazy as _

class CustomDateInput(forms.DateInput):
    def __init__(self, attrs=None, **kwargs):
        if 'null' in kwargs:
            self.null = kwargs.pop('null')
        else:
            self.null = False

        super().__init__(attrs=attrs, **kwargs)

    def format(self, value):
        if value is None:
            return ''
        return value.strftime('%d.%m.%Y')

    def value_from_datadict(self, data, files, name):
        if data:
            return super().value_from_datadict(data, files, name)
        return None
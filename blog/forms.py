from django import forms
from django.core.exceptions import ValidationError
from .models import Comment
from .models import CallBooking
import datetime
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

def get_time_intervals():
    return [
        ('09:00', '9:00 - 10:00'),
        ('10:00', '10:00 - 11:00'),
        ('11:00', '11:00 - 12:00'),
        ('12:00', '12:00 - 13:00'), 
        ('13:00', '13:00 - 14:00'),
        ('14:00', '14:00 - 15:00'),
        ('15:00', '15:00 - 16:00'),
        ('16:00', '16:00 - 17:00'),
        ('17:00', '17:00 - 18:00'),
        ('18:00', '18:00 - 19:00'),
        ('19:00', '19:00 - 20:00'),
    ]

# Form for creating or updating CallBooking instances.
class CallBookingForm(forms.ModelForm):
    client_name = forms.CharField(label='Ім\'я клієнта')
    client_email = forms.EmailField(label='Електронна пошта клієнта')
    phone_number = forms.CharField(label='Номер телефону')
    details = forms.CharField(label='Деталі', widget=forms.Textarea)
    call_date = forms.DateField(label='Дата', widget=DateInput())
    call_time = forms.ChoiceField(choices=get_time_intervals(), label='Оберіть час')

    class Meta:
        model = CallBooking
        fields = ['client_name', 'client_email', 'phone_number', 'details', 'call_date', 'call_time']
        widgets = {
            'call_time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['call_date'] = date.today()
        self.fields['call_date'].required = True

    def clean_call_date(self):
        call_date = self.cleaned_data['call_date']
        if call_date <= date.today():
            raise ValidationError('Дата дзвінка не може бути ні минулою, ні сьогоднішньою')
        return call_date


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
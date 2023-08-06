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
        ('09:00', '9:00 AM - 10:00 AM'),
        ('10:00', '10:00 AM - 11:00 AM'),
        ('11:00', '11:00 AM - 12:00 PM'),
        ('12:00', '12:00 AM - 1:00 PM'), 
        ('1:00', '1:00 PM - 2:00 PM'),
        ('2:00', '2:00 PM - 3:00 PM'),
        ('3:00', '3:00 PM - 4:00 PM'),
        ('4:00', '4:00 PM - 5:00 PM'),
        ('5:00', '5:00 PM - 6:00 PM'),
        ('6:00', '6:00 PM - 7:00 PM'),
        ('7:00', '7:00 PM - 8:00 PM'),
    ]

# Form for creating or updating CallBooking instances.
class CallBookingForm(forms.ModelForm):
    call_time = forms.ChoiceField(choices=get_time_intervals, label='Select time')

    class Meta:
        model = CallBooking
        fields = ['client_name', 'client_email', 'phone_number', 'details', 'call_date', 'call_time']
        widgets = {
            'call_date': DateInput(),
            'call_time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['call_date'] = date.today()
        self.fields['call_date'].required = True

    def clean_call_date(self):
        call_date = self.cleaned_data['call_date']
        if call_date <= date.today():
            raise ValidationError('The call date cannot be in the past or today!')
        return call_date

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
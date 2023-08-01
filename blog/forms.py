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

# Form for creating or updating CallBooking instances.
class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['client_name', 'client_email', 'phone_number', 'details', 'call_date']
        widgets = {
            'call_date': DateInput(),
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
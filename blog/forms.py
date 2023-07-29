from django import forms
from .models import CallBooking

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['client_name', 'client_email', 'phone_number', 'details', 'call_date', 'call_time']
        widgets = {
            'call_date': DateInput(),
            'call_time': TimeInput(),
        }

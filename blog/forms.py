from django import forms
from .models import Comment
from .models import CallBooking
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

# Form for creating or updating CallBooking instances.
class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['client_name', 'client_email', 'phone_number', 'details', 'call_date', 'call_time']
        widgets = {
            'call_date': DateInput(),
            'call_time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['call_date'] = datetime.date.today()
        self.fields['call_time'].required = True 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
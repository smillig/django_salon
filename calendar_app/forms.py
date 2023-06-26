import datetime
from django import forms
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from captcha.fields import CaptchaField

from .models import CalendarUser, Event

class CalendarUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
        ("O", "---"),
        ("M", gettext_lazy("Male")),
        ("F", gettext_lazy("Female")),
        ("O", gettext_lazy("Other"))
    ]
    first_name = forms.CharField(label=gettext_lazy("First Name"), max_length=100, help_text=gettext_lazy("Required"))
    last_name = forms.CharField(label=gettext_lazy("Last Name"), required=False, max_length=100)
    email = forms.EmailField(label=gettext_lazy("Email address"), help_text=gettext_lazy("Required"))
    phone_num = forms.CharField(label=gettext_lazy("Phone Number"), required=False, max_length=13)
    gender = forms.ChoiceField(label=gettext_lazy("Gender"), required=False, choices=GENDER_CHOICES)
    address = forms.CharField(label=gettext_lazy("Address"), required=False, widget=forms.Textarea, max_length=255)
    date_of_birth = forms.DateField(label=gettext_lazy("Date of Birth"), required=False, \
                                    widget=forms.SelectDateWidget(years=range(datetime.date.today().year - 110, datetime.date.today().year)))
    captcha = CaptchaField()


    class Meta:
        model = CalendarUser
        fields = ("username", "first_name", "last_name", "email", "phone_num", "gender", "address", "date_of_birth", "captcha")

    

class CalendarUserChangeForm(UserChangeForm):

    class Meta:
        model = CalendarUser
        fields = ("username", "email")


class CreateEventForm(forms.ModelForm):

    name = forms.CharField(label=gettext_lazy("Appointment Name"), max_length=255)
    start = forms.DateTimeField(label=gettext_lazy("Start"), widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end = forms.DateTimeField(label=gettext_lazy("End"), widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


    class Meta:
        model = Event
        fields = ("name", "start", "end")

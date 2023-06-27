import datetime
from django import forms
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from captcha.fields import CaptchaField, CaptchaTextInput

from .models import CalendarUser, Event


# Custom user form for requested information from salon
class CalendarUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
        ("O", "---"),
        ("M", gettext_lazy("Male")),
        ("F", gettext_lazy("Female")),
        ("O", gettext_lazy("Other"))
    ]
    username = forms.CharField(label=gettext_lazy("Username"), max_length=150, \
                               help_text=gettext_lazy("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),\
                                widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': ("Username")}))
    first_name = forms.CharField(label=gettext_lazy("First Name"), max_length=100, help_text=gettext_lazy("Required"), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': ("First Name")}))
    last_name = forms.CharField(label=gettext_lazy("Last Name"), required=False, max_length=100, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': ("Last Name")}))
    email = forms.EmailField(label=gettext_lazy("Email address"), help_text=gettext_lazy("Required"), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': gettext_lazy("Email Address")}))
    phone_num = forms.CharField(label=gettext_lazy("Phone Number"), required=False, max_length=13, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':gettext_lazy ("Phone Number")}))
    gender = forms.ChoiceField(label=gettext_lazy("Gender"), required=False, choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': "form-control", 'placeholder': gettext_lazy("Gender")}))
    address = forms.CharField(label=gettext_lazy("Address"), required=False, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': gettext_lazy("Address")}), max_length=255)
    date_of_birth = forms.DateField(label=gettext_lazy("Date of Birth"), required=False, \
                                    widget=forms.SelectDateWidget(years=range(datetime.date.today().year - 110, datetime.date.today().year),attrs={'class': "form-control"}))
    captcha = CaptchaField(label=gettext_lazy("Captcha: Confirm you're not a robot."), widget=CaptchaTextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label=gettext_lazy("Password"), help_text=gettext_lazy("<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"), widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': gettext_lazy("Password")}), max_length=254)
    password2 = forms.CharField(label=gettext_lazy("Confirm Password"),help_text=gettext_lazy("Enter the same password as before, for verification."), widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': gettext_lazy("Confirm Password")}), max_length=254)


    class Meta:
        model = CalendarUser
        fields = ("username", "first_name", "last_name", "email", "phone_num", "gender", "address", "date_of_birth", "captcha")



# Custom login form so CSS "form-control" can keep style and look with theme
class CalendarUserLoginForm(AuthenticationForm):
    username = forms.CharField(label=gettext_lazy("Username"), max_length=150, \
                                widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': gettext_lazy("Username")}))
    password = forms.CharField(label=gettext_lazy("Password"), max_length=150, \
                                widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': gettext_lazy("Password")}))
    class Meta:
        model = CalendarUser
        fields = ('username', 'password')
        


# TODO: Allow users to update information
class CalendarUserChangeForm(UserChangeForm):

    class Meta:
        model = CalendarUser
        fields = ("username", "email")



# TODO: Create page for users to create events
class CreateEventForm(forms.ModelForm):

    name = forms.CharField(label=gettext_lazy("Appointment Name"), max_length=255)
    start = forms.DateTimeField(label=gettext_lazy("Start"), widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end = forms.DateTimeField(label=gettext_lazy("End"), widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


    class Meta:
        model = Event
        fields = ("name", "start", "end")

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CalendarUser, Calendar, Event
from .forms import CalendarUserCreationForm, CalendarUserChangeForm

# Register your models here.
@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['id', 'location']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start', 'end']

@admin.register(CalendarUser)
class CustomUserAdmin(UserAdmin):
    add_form = CalendarUserCreationForm
    form = CalendarUserChangeForm
    model = CalendarUser
    list_display = ["username", "email", "first_name", "last_name", "phone_num", "gender", "address", "date_of_birth"]
    fieldsets = [
        (
            None, 
                {'fields': ('username', 'password')}),
        (
            ('Personal info'), {'fields': ('first_name', 'last_name', 'email', "phone_num", "gender", "address", "date_of_birth")}),
        (
            ('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (
            ('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]

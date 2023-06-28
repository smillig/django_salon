import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_user
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Event, CalendarUser
from .forms import CalendarUserCreationForm, CalendarUserLoginForm, CalendarUserChangeForm

# Custom sign up form since this works but not for authentication
class SignUpView(CreateView):
    form_class = CalendarUserCreationForm
    success_url = reverse_lazy("calendar")
    template_name = "registration/signup.html"
    

# Custom login form so that css is applied from form
def login(request):
    if request.method == "POST":
        login_form = CalendarUserLoginForm(request.POST)
        print(login_form.is_valid())
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_model = CalendarUser.objects.get(username=username)
            if user_model.check_password(password):
                login_user(request, user_model)
                return redirect(reverse_lazy('calendar'))
        else:
            form = CalendarUserLoginForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'errors': login_form.errors})
    else:
        form = CalendarUserLoginForm()
        return render(request, 'registration/login.html', {'form': form})

def user_info(request):
    form = CalendarUserChangeForm()
    if request.method == "POST":
        update_form = CalendarUserChangeForm(request.POST)
        if update_form.is_valid():
            password = request.POST.get('password')
            user_model = CalendarUser.objects.get(username=request.user.username)
            if user_model.check_password(password):
                # Tuple of fields we don't want looped over
                loop_skips = ("password", "new_password_1", "new_password_2", "date_of_birth_year", "date_of_birth_day", "date_of_birth_month")
                for item in update_form.fields:
                    # Change only values that are populated
                    if (request.POST.get(item) not in (None, "", "None", "-") and (item not in loop_skips)):
                        setattr(user_model, item, request.POST.get(item))
                        user_model.save()
                # date_of_birth must be reconstructed from 3 different places
                if request.POST.get('date_of_birth_month') not in (None, "", "None", "-") and \
                    request.POST.get('date_of_birth_day') not in (None, "", "None", "-") and \
                        request.POST.get('date_of_birth_year') not in (None, "", "None", "-"):
                    user_model.date_of_birth = datetime.datetime(year=int(request.POST.get('date_of_birth_year')), \
                                                                 month=int(request.POST.get('date_of_birth_month')), \
                                                                    day=int(request.POST.get('date_of_birth_day')))
                    user_model.save()
                # TODO: check for new_password validate and set new password       
            return redirect(reverse_lazy('user_info'))
        else:
            errors = update_form.errors
            context = {'errors': errors, 'form': form}
            return render(request, 'user_info.html', context)
    else:
        return render(request, 'user_info.html', {'form': form})

# Get standard Calendar page
def view_calendar(request):
    return render(request, 'calendar.html')

# Allows FullCalendar to populate with events via JS
def all_events(request):                                                                                                 
    all_events = Event.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                     
    return JsonResponse(out, safe=False)

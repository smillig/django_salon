from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Event, CalendarUser
from .forms import CalendarUserCreationForm, CalendarUserLoginForm

class SignUpView(CreateView):
    form_class = CalendarUserCreationForm
    success_url = reverse_lazy("calendar")
    template_name = "registration/signup.html"
    

def login(request):
    if request.method == "POST":
        login_form = CalendarUserLoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_model = CalendarUser.objects.get(username=username)
            if user_model.check_password(password):
                login(request, user_model)
                return redirect(reverse_lazy('calendar'))
        else:
            form = CalendarUserLoginForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'errors': login_form.errors})
    else:
        form = CalendarUserLoginForm()
        return render(request, 'registration/login.html', {'form': form})

def view_calendar(request):
    return render(request, 'calendar.html')

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

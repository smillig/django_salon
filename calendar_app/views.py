from django.shortcuts import render
from django.http import JsonResponse
from .models import Calendar, Event

# Create your views here.
def view_calendar(request):
    # Retrieve the calendar object from the database
    # calendar = Calendar.objects.get(location='default')
    # eventList = Event.objects.all()
    return render(request, 'calendar.html')

def calendar(request):
    all_events = Event.objects.all()
    calendar = Calendar.objects.get(location='default')
    context = {
        "calendar": calendar,
        "events": all_events,
    }
    return render(request,'calendar.html', context)

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
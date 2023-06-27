import datetime
from django.test import TestCase
from .models import CalendarUser, Event, Calendar

# Create your tests here.
class CalendarAppUnitTestCase(TestCase):

    def setUp(self) -> None:
        user = CalendarUser.objects.create(username = "test_case_user", email = "testuser@test.com", first_name = "Test", password = "reallyinsecurepassword")
        calendar = Calendar.objects.create(location="test")
        Event.objects.create(name='test event', user=user, calendar=calendar, \
                            start=datetime.datetime.now(tz=datetime.timezone.utc), \
                                end=(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)))
        return super().setUp()
    
    def test_user_model(self):
        test_user = CalendarUser.objects.get(id=1)
        name_label = test_user._meta.get_field('first_name').verbose_name
        self.assertEqual(name_label, 'first name')

    def test_calendar_model(self):
        test_calendar = Calendar.objects.get(id=1)
        location_label = test_calendar._meta.get_field('location').verbose_name
        self.assertEqual(location_label, 'location')

    def test_event_model(self):
        test_event = Event.objects.get(id=1)
        event_label = test_event.name
        self.assertEqual(event_label, 'test event')

    def test_can_get_calendar(self):
        response = self.client.get('/calendar/')
        self.assertTemplateUsed(response, 'calendar.html')

    def test_can_get_all_events(self):
        response = self.client.get('/all_events/')
        self.assertEqual(response.json()[0]['title'], 'test event')

    def test_can_get_login_page(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_can_get_signup_page(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_can_get_user_info_page(self):
        response = self.client.get('/user_info/')
        self.assertTemplateUsed(response, 'user_info.html')

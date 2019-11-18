from django.conf.urls import url
from . import views

app_name = 'college'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^student-application/$', views.student_application, name='student-application'),
    url(r'^student-registration/$', views.student_registration, name='student-registration'),
    url(r'^staff-registration/$', views.staff_registration, name='staff-registration'),
    # url(r'^login/$', views.)

    ]
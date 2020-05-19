from django.conf.urls import include, url
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^test/$', testing, name='test'),
    url(r'^employee/new/$', create_employee, name='create_employee'),
    url(r'^employee_detail/(?P<pk>\d+)/$', employee_detail, name='employee_detail'),
    url(r'^suggest-a-flavour/$', suggest),
]

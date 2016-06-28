from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^Person/$', views.PersonAPI.as_view()),
    url(r'^Person/(?P<id>[0-9]+)/', views.PersonAPI.as_view()),
]

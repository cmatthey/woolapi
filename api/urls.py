from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/volunteers$', views.volunteer_list),
]
from django.urls import path
from . import views

urlpatterns = [
    path('freelancer/profile/',views.freelance_profile,name='freelance_profile'),
    path('client/profile/',views.client_profile,name='client_profile'),
    path("client/profile/edit/",views.edit_profile, name="edit_profile"),
]
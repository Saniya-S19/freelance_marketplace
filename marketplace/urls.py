from django.urls import path
from marketplace import views as marketplace_views

urlpatterns = [
    path('pitch/create/', marketplace_views.create_pitch, name="create_pitch"),
]
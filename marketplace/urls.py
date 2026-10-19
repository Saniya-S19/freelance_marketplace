from django.urls import path
from marketplace import views as marketplace_views

urlpatterns = [
    path('pitch/create/', marketplace_views.create_pitch, name="create_pitch"),
    path('pitch/<int:pitch_id>/update/', marketplace_views.update_pitch_status, name="update_pitch_status"),
]
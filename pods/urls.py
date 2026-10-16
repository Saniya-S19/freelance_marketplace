from django.urls import path
from accounts import views as accounts_views
from pods import views as pods_views

urlpatterns = [
    path('freelancer_dashboard/', accounts_views.freelancer, name="freelancer"),
    path('pods/create/', pods_views.create_pod, name="create_pod"),
]
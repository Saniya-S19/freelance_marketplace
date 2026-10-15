from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.login_page, name = "login"),
    path('logout/',views.logout, name = "logout"),
    path('signup/',views.signup, name = "signup"),
    path('find-freelancers/', views.find_freelancers, name='find_freelancers'),

    path('client_dashboard/',views.client, name='client'),
    path('freelancer_dashboard/',views.freelancer, name='freelancer'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('client_dashboard/', views.client, name="client"),
    path('freelancer_dashboard/', views.freelancer, name="freelancer"),
    path('find-freelancers/', views.find_freelancers, name="find_freelancers"),
]
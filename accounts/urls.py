from django.urls import path
from accounts import views as accounts_views  
from pods import views as pods_views
from marketplace import views as marketplace_views

urlpatterns = [
    path('', accounts_views.home, name="home"),
    path('login/', accounts_views.login_view, name="login"),
    path('signup/', accounts_views.signup_view, name="signup"),
    path('logout/', accounts_views.logout_view, name="logout"),
    path('client_dashboard/', accounts_views.client, name="client"),
    path('freelancer_dashboard/', accounts_views.freelancer, name="freelancer"),
    path('find-freelancers/', accounts_views.find_freelancers, name="find_freelancers"),
    path('pods/create/', pods_views.create_pod, name="create_pod"),
    path('pitch/create/', marketplace_views.create_pitch, name="create_pitch"),
    path('pitch/<int:pitch_id>/update/', marketplace_views.update_pitch_status, name="update_pitch_status"),
]
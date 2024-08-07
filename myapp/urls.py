from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("signup/", views.user_signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("Aboutme/", views.Aboutme, name="Aboutme"),
]

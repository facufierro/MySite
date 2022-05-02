from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.login, name="login"),
    # path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
]

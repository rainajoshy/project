from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="packages/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("packages/", views.package_list, name="package_list"),
    path("packages/add/", views.add_package, name="add_package"),
    path("packages/<int:pk>/edit/", views.edit_package, name="edit_package"),
    path("packages/<int:pk>/delete/", views.delete_package, name="delete_package"),
]

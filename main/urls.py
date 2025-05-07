from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importing auth views for login/logout

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('', include('your_app_name.urls')),

]


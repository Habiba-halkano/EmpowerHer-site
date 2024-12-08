from django.urls import path
from .views import register_view, login_view, logout_view, home_view, contact_view
from dashboard.views import home, dashboard


urlpatterns = [
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('welcome/', home_view, name='welcome'),
    path('home/', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contact/', contact_view, name='contact'),
]
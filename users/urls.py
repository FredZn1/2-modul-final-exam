from django.urls import path
from .views import UserLoginView, UserLogoutView, UpdateProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
]

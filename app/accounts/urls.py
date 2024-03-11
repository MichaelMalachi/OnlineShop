from django.urls import path, include
from accounts.views import MyProfileView
from accounts.views import SingUpView
from accounts.views import ActivateView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('my-profile/<int:pk>', MyProfileView.as_view(), name='my-profile-link'),
    path('sing-up/', SingUpView.as_view(), name='sing-up-link'),
    path('activate/<uuid:username>', ActivateView.as_view(), name='activate-link'),

]

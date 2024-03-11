from django.urls import path
from general.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home-link"),

]

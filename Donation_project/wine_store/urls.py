# LIBRARIES
from django.urls import path

# VIEW FUNCTIONS
from .views import (
    home,
    success,
    cancel,
    checkout,
)

# URL PATTERS
urlpatterns = [
    path('', home, name="home"),
    path('success/', success, name="success"),
    path('cancel/', cancel, name="cancel"),
    path('checkout/', checkout, name="checkout"),
]

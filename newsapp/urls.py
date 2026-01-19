
from django.urls import path
from .views import helleView

urlpatterns = [
    path('', helleView, name="askdsa")
]

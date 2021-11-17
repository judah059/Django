from django.urls import path
from .views import acricles, archive
urlpatterns = [
    path("", acricles),
    path("archive/", archive),
]

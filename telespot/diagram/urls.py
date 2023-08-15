from django.urls import path
from . import views

urlpatterns = [
    path("diagram/", views.diagram_page, name="diagram_page"),
]

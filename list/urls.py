from django.urls import path
from . import views

app_name = "list"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:zipcode>", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("add", views.add, name="add"),
]

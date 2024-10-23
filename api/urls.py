# This file is used to define the urls for the api app
from django.urls import path , include
from contact import views


urlpatterns = [
    path('home/',views.home),
    path('get-messages/',views.get_messages),
    path('message/',views.MessageAPI.as_view()),
]

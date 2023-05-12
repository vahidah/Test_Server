from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import (testAPI)

urlpatterns = [

    path("login/", obtain_auth_token, name='login'),
]



from django.urls import path
from .views import *
from .forms import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_core_view'),
    path('createClient/', createClient, name='createClient'),
]
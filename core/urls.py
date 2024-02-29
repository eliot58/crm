from django.urls import path
from .views import *
from .forms import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_core_view'),
    path('createClient/', createClient, name='createClient'),
    path('updateClient/<int:id>/', updateClient, name='updateClient'),
    path('take/<int:id>/', take, name='take'),
    path('refuse/<int:id>/', refuse, name='refuse'),
    path('no_target/<int:id>/', no_target, name='no_target'),
    path('get_logs/<int:id>/', get_logs, name='get_logs'),
    path('sendCalc/<int:id>/', send_calc, name='send_calc'),
    path('validate/', validate, name='validate'),
    path('createDiler/', createDiler, name='create_diler'),
]
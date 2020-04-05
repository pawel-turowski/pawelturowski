from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views



urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('my_account/', login_required(views.MyAccount.as_view()), name='my_account'),
]
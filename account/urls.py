from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'account'

urlpatterns = [
    # path('login/', views.login, name="login"),
    # path('login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('login/', LoginView.as_view(), name='login'),
]

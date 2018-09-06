from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'account'

login_context = dict(
    template_name='account/login.html',
)

logout_context = dict(
    template_name='account/logout.html',
)
urlpatterns = [
    # path('login/', views.login, name="login"),
    # path('login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('login/', LoginView.as_view(**login_context), name='login'),
    # path('login/', LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(**logout_context), name='logout'),
]

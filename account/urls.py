from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
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
    path('register/', views.register, name='register'),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    # TODO:: 了解类视图的写法，以及如何传入参数！！
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]

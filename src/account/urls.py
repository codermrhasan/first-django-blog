from django.urls import path
from .views import(
    signup,
    profile,
    delete_account
)
from django.contrib.auth.views import(
    LoginView,
    LogoutView
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_account, name='delete_account')
]

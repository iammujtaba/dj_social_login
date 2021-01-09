from django.urls import path
from accounts.views import AllUsers, CreateAccount, CurrentUser

app_name = 'users'

urlpatterns = [
    path('create/', CreateAccount.as_view(),name = "create_user"),
    path('all/', AllUsers.as_view(), name="all"),
    path('currentUser/', CurrentUser.as_view(), name="current"),
]

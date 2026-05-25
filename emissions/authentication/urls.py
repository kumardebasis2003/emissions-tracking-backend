from django.urls import path
from .views import SuperuserLoginView, SuperuserTokenRefreshView

urlpatterns = [
    path('login/', SuperuserLoginView.as_view(), name='superuser-login'),
    path('refresh/', SuperuserTokenRefreshView.as_view(), name='token-refresh'),
]
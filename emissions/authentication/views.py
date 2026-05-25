from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import SuperuserTokenSerializer

class SuperuserLoginView(TokenObtainPairView):
    """Login endpoint restricted to superusers only"""
    serializer_class = SuperuserTokenSerializer

class SuperuserTokenRefreshView(TokenRefreshView):
    """Token refresh endpoint (inherits superuser validation from initial login)"""
    pass
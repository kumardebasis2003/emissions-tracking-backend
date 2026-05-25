from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

class SuperuserTokenSerializer(TokenObtainPairSerializer):
    """Overrides default JWT login to enforce superuser-only access"""
    
    def validate(self, attrs):
        # 1. Validate username & password first
        data = super().validate(attrs)
        
        # 2. Enforce superuser restriction
        if not self.user.is_superuser:
            raise AuthenticationFailed({
                "detail": "Access denied. Only superusers can authenticate."
            })
            
        return data
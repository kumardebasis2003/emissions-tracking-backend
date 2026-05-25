from django.contrib.auth import get_user_model

User = get_user_model()

class AuthService:
    @staticmethod
    def verify_superuser_access(username: str) -> bool:
        """Checks if a username belongs to a superuser"""
        try:
            return User.objects.filter(username=username, is_superuser=True).exists()
        except Exception:
            return False

    @staticmethod
    def get_superuser_id(username: str) -> int | None:
        """Returns user ID if superuser, else None"""
        try:
            user = User.objects.get(username=username, is_superuser=True)
            return user.id
        except User.DoesNotExist:
            return None
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema

from .models import AuditLog
from .serializers import AuditLogSerializer


@extend_schema(
    tags=['Audit Logs']
)
class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AuditLog.objects.all().order_by('-changed_at')

    serializer_class = AuditLogSerializer

    permission_classes = [AllowAny]
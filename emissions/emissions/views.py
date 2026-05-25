from rest_framework import viewsets
from .models import EmissionRecord
from .serializers import EmissionDetailSerializer

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiResponse
)

from drf_spectacular.types import OpenApiTypes


@extend_schema_view(
    list=extend_schema(
        summary="List emission records",
        description="Paginated list with filtering by scope, status, and full-text search.",
        parameters=[
            OpenApiParameter(
                name='scope',
                description='Scope 1, Scope 2, or Scope 3',
                type=str,
                location='query'
            ),
        ]
    ),
)
class EmissionRecordViewSet(viewsets.ModelViewSet):

    queryset = EmissionRecord.objects.all()

    serializer_class = EmissionDetailSerializer
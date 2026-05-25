from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Company
from .serializers import (
    CompanySerializer,
    DashboardSerializer
)

from .services import get_dashboard_stats


# ==========================================
# Company CRUD API
# ==========================================

class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()

    serializer_class = CompanySerializer

    permission_classes = [AllowAny]


# ==========================================
# Dashboard Summary API
# ==========================================

class DashboardView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        company = Company.objects.first()

        if not company:

            return Response({
                "error": "No company found"
            })

        stats = get_dashboard_stats(company)

        serializer = DashboardSerializer(stats)

        return Response(serializer.data)
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from rest_framework.routers import DefaultRouter

# ← NO 'apps.' PREFIX IN IMPORTS
from emissions.views import EmissionRecordViewSet
from audits.views import AuditLogViewSet

router = DefaultRouter()
router.register(r'emissions', EmissionRecordViewSet, basename='emissions')
router.register(r'audit-logs', AuditLogViewSet, basename='audit')

def home(request):
    return JsonResponse({
        "message": "ESG Insights Hub Backend Running Successfully",
        "version": "1.0.0",
        "docs": "/api/docs/swagger/",
        "status": "healthy"
    })

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    
    # Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Authentication
    path('api/auth/', include('authentication.urls')),
    
    # API Endpoints
    path('api/', include([
        path('', include(router.urls)),
        path('dashboard/', include('companies.urls')),
        path('review/', include('reviews.urls')),
        path('upload/', include('ingestion.urls')),
    ])),
]
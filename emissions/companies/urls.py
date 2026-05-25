from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    DashboardView,
    CompanyViewSet
)

router = DefaultRouter()

router.register(
    r'companies',
    CompanyViewSet,
    basename='companies'
)

urlpatterns = [

    path(
        'summary/',
        DashboardView.as_view(),
        name='dashboard-summary'
    ),

    path('', include(router.urls)),
]
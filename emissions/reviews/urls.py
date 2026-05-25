from django.urls import path
from .views import approve_view, reject_view, lock_view

urlpatterns = [
    path('<int:pk>/approve/', approve_view, name='review-approve'),
    path('<int:pk>/reject/', reject_view, name='review-reject'),
    path('<int:pk>/lock/', lock_view, name='review-lock'),
]
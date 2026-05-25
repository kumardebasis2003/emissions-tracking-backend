from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Approve record",
    description="Sets status to approved.",
)
@api_view(['POST'])
def approve_view(request, pk):

    return Response({
        "status": "approved",
        "id": pk
    })


@extend_schema(
    summary="Reject record",
    description="Sets status to rejected.",
)
@api_view(['POST'])
def reject_view(request, pk):

    return Response({
        "status": "rejected",
        "id": pk
    })


@extend_schema(
    summary="Lock record",
    description="Locks the record.",
)
@api_view(['POST'])
def lock_view(request, pk):

    return Response({
        "locked": True,
        "id": pk
    })
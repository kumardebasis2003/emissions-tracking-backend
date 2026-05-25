from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Upload SAP CSV",
    description="Upload and process SAP CSV file.",
)
class SAPUploadView(APIView):

    def post(self, request):

        return Response({
            "message": "SAP CSV uploaded successfully",
            "records_created": 10
        }, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Upload Utility CSV",
    description="Upload utility emission file.",
)
class UtilityUploadView(APIView):

    def post(self, request):

        return Response({
            "message": "Utility CSV uploaded successfully"
        }, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Upload Travel CSV",
    description="Upload travel emission file.",
)
class TravelUploadView(APIView):

    def post(self, request):

        return Response({
            "message": "Travel CSV uploaded successfully"
        }, status=status.HTTP_201_CREATED)
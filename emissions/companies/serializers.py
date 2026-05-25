from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']

class DashboardSerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    approved = serializers.IntegerField()
    pending = serializers.IntegerField()
    rejected = serializers.IntegerField()
    suspicious = serializers.IntegerField()
    total_emissions = serializers.FloatField()
    by_scope = serializers.JSONField()
    by_source = serializers.JSONField()
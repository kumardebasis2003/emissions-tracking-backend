from rest_framework import serializers
from .models import EmissionRecord


class EmissionListSerializer(serializers.ModelSerializer):

    source = serializers.CharField(
        source='source_record.source.source_type',
        read_only=True
    )

    class Meta:

        model = EmissionRecord

        fields = [
            'id',
            'source',
            'scope',
            'activity_type',
            'facility',
            'quantity',
            'unit',
            'total_emissions',
            'review_status',
            'suspicious_flag',
            'is_locked',
            'created_at'
        ]


class EmissionDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = EmissionRecord

        fields = '__all__'

        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]
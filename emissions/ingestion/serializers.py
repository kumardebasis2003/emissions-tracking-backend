from rest_framework import serializers

class SAPUploadSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    file = serializers.FileField()

class UtilityUploadSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    file = serializers.FileField()
    utility_type = serializers.ChoiceField(choices=['electricity', 'gas', 'water'], default='electricity')

class TravelUploadSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    employee = serializers.CharField(max_length=100)
    travel_type = serializers.CharField(max_length=50)
    from_location = serializers.CharField(max_length=100)
    to_location = serializers.CharField(max_length=100)
    distance_km = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()
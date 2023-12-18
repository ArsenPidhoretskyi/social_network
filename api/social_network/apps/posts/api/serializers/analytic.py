from rest_framework import serializers


class AnalyticSerializer(serializers.Serializer):
    created = serializers.DateField()
    count = serializers.IntegerField()

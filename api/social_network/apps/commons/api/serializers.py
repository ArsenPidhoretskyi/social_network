from rest_framework.serializers import Serializer as RestFrameworkSerializer


class CoreSerializer(RestFrameworkSerializer):
    def create(self, validated_data):
        raise NotImplementedError("Do not use create directly")

    def update(self, instance, validated_data):
        raise NotImplementedError("Do not use update directly")

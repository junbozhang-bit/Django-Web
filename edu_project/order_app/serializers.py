from rest_framework import serializers


class OrdersSerializers(serializers.Serializer):
    class_type = serializers.IntegerField(required=True)

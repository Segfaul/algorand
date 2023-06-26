from rest_framework import serializers


class GraphicData(serializers.Serializer):
    parameter = serializers.IntegerField()

    def validate_parameter(self, value):
        try:
            value = int(value)
        except ValueError:
            raise serializers.ValidationError('Invalid value')

        finally:
            return value

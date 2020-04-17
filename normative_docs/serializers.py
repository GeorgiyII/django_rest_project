from rest_framework import serializers
from normative_docs.models import (
    StallMark,
    BoltArea,
    ResCrushing,
    ResShear
)


class StallMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StallMark
        fields = '__all__'


class BoltAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoltArea
        fields = '__all__'


class ResCrushingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResCrushing
        fields = '__all__'


class ResShearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResShear
        fields = '__all__'

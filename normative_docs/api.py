from normative_docs.models import (
    StallMark,
    ResShear,
    ResCrushing,
    BoltArea
)
from rest_framework import viewsets, permissions
from normative_docs.serializers import (
    StallMarkSerializer,
    BoltAreaSerializer,
    ResCrushingSerializer,
    ResShearSerializer
)


class StallMarkViewSet(viewsets.ModelViewSet):
    queryset = StallMark.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StallMarkSerializer


class BoltAreaViewSet(viewsets.ModelViewSet):
    queryset = BoltArea.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoltAreaSerializer


class ResShearViewSet(viewsets.ModelViewSet):
    queryset = ResShear.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResShearSerializer


class ResCrushingViewSet(viewsets.ModelViewSet):
    queryset = ResCrushing.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResCrushingSerializer

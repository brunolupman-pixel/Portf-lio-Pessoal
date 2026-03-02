from rest_framework import viewsets
from .models import AcademicBackground
from .serializers import AcademicBackgroundSerializer


class AcademicBackgroundViewSet(viewsets.ModelViewSet):
    queryset = AcademicBackground.objects.all()
    serializer_class = AcademicBackgroundSerializer

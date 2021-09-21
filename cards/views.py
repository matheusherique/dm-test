from rest_framework import viewsets

from .models import Solicitation
from .serializers import SolicitationSerializer


class SolicitationViewSet(viewsets.ModelViewSet):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer
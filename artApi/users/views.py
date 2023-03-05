from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['username']
    filterset_fields = ['username']
    ordering_fields = '__all__'
    ordering = ['username']

    # Permissions
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.permissions import IsOwnerOrReadOnly
from goods.models import Category, Good
from api.serializers import (
    CategoryDisplaySerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
    GoodDisplaySerializer,
    GoodCreateUpdateSerializer,
    UserShortDisplaySerializer,
)

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]

    def get_serializer_class(self):
        if self.action == 'create':
            return CategoryCreateSerializer
        if self.action == 'update':
            return CategoryUpdateSerializer
        return CategoryDisplaySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return GoodCreateUpdateSerializer
        return GoodDisplaySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(moderator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserShortDisplaySerializer

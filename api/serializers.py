from django.contrib.auth import get_user_model
from rest_framework import serializers

from goods.models import Category, Good

User = get_user_model()


class UserShortDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class CategoryDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'slug', 'name')


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'name')

    def to_representation(self, instance):
        return CategoryDisplaySerializer(instance).data


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

    def to_representation(self, instance):
        return CategoryDisplaySerializer(instance).data


class GoodDisplaySerializer(serializers.ModelSerializer):
    category = CategoryDisplaySerializer()
    creator = UserShortDisplaySerializer()
    moderator = UserShortDisplaySerializer()

    class Meta:
        model = Good
        fields = '__all__'


class GoodCreateUpdateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Good
        fields = ('name', 'category', 'description')

    def to_representation(self, instance):
        return GoodDisplaySerializer(instance).data

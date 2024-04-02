from core.models import Page, Page_Category, User, Category, Comment

from rest_framework import serializers

class WrapperSerializer(serializers.Serializer):
    """
        Обертка для отправки ответа согласно документации
    """
    ok = serializers.BooleanField
    result = serializers.JSONField(encoder=None)

class User(serializers.Serializer):
    """
        Сериалайзер для модели User
    """
    class Meta:
        model = User
        fields = ('__all__')

class PageSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для модели Page
    """
    class Meta:
        model = Page
        fields = ('__all__')

class PageCategorySerializer(serializers.ModelSerializer):
    """
        Сериалайзер для модели Page_Category
    """
    class Meta:
        model = Page_Category
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    """
        Сериалайзер для модели Category
    """
    class Meta:
        model = Category
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для модели Comment
    """
    class Meta:
        model = Comment
        fields = ('__all__')

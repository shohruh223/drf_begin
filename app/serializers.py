from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, Serializer
from app.models import Product, Category, Comment


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()


class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        exclude = ()


class CommentModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        exclude = ()




















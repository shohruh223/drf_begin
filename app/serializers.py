from rest_framework.serializers import ModelSerializer
from app.models import Product


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()
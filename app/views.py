from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from app.models import Product, Category, Comment
from app.permission import IsAuthOrReadOnlyPermission
from app.serializers import ProductModelSerializer, CategoryModelSerializer, CommentModelSerializer


# class ProductView(APIView):
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductModelSerializer(products, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ProductModelSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data={'message':'This data is bad request'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDetailView(APIView):
#
#     def get(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         if product:
#             serializer = ProductModelSerializer(product)
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(data={'message':'This data is not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         serializer = ProductModelSerializer(instance=product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(data={'message':'This data is not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         if product:
#             product.delete()
#             return Response(data={'message':'This data is successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             Response(data={'message':'This data is not found'}, status=status.HTTP_404_NOT_FOUND)


# class ProductView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#
#
# class ProductRetrieveView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated, ]


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAdminUser, )


# class CommentView(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentModelSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthOrReadOnlyPermission, )

















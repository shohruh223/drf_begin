
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import ProductView, CategoryView, CommentView

router = DefaultRouter()
router.register('product', ProductView)
router.register('category', CategoryView)
router.register('comment', CommentView)


urlpatterns = [
    # path('product/', ProductView.as_view()),
    # path('product/<int:pk>', ProductDetailView.as_view())
    # path('product/', ProductView.as_view()),
    # path('product/<int:pk>', ProductRetrieveView.as_view()),
    path('', include(router.urls))
]




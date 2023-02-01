
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import  ProductView


router = DefaultRouter()
router.register('', ProductView)


urlpatterns = [
    # path('product/', ProductView.as_view()),
    # path('product/<int:pk>', ProductDetailView.as_view())
    # path('product/', ProductView.as_view()),
    # path('product/<int:pk>', ProductRetrieveView.as_view()),
    path('', include(router.urls))
]

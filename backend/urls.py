from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Auth.views import UserProfileVIew
from Shop.views import ShopItemView, CartView, CartDetailView, FavoriteView, FavoriteDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'items', ShopItemView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    path('api/user/profile/', UserProfileVIew.as_view(),
         name='user_profile_view'),

    path('api/user/cart/', CartView.as_view(), name='user_cart_view'),
    path('api/user/cart/item/<int:pk>/', CartDetailView.as_view(),
         name='user_cart_view'),

    path('api/user/favorite/', FavoriteView.as_view(),
         name='user_favorite_view'),
    path('api/user/favorite/<int:pk>/', FavoriteDetailView.as_view(),
         name='user_favorite_detail_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

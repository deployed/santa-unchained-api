from django.urls import path
from rest_framework.routers import DefaultRouter

from santa_unchained.wishes.api_views import (
    PackageDistributionViewSet,
    PackageViewSet,
    WishListViewSet,
)
from santa_unchained.wishes.views import (
    WishListDetailView,
    WishListFormView,
    WishListSuccessView,
)

app_name = "wishes"
router = DefaultRouter()
router.register(r"wishlists", WishListViewSet, basename="wishlist")
router.register(r"packages", PackageViewSet, basename="package")
router.register(
    r"distribution", PackageDistributionViewSet, basename="package-distribution"
)

urlpatterns = [
    path("", WishListFormView.as_view(), name="wishlist"),
    path("success/<slug:slug>/", WishListSuccessView.as_view(), name="success"),
    path("<slug:slug>/", WishListDetailView.as_view(), name="wishlist-detail"),
]

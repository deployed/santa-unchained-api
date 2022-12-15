from django.db.transaction import atomic
from drf_mixin_tools.mixins import ActionSerializerClassMixin
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from santa_unchained.wishes.constants import PackageStatuses, WishListStatuses
from santa_unchained.wishes.models import Package, WishList
from santa_unchained.wishes.serializers import (
    PackageDetailSerializer,
    PackageDistributionSerializer,
    PackageSendBodySerializer,
    PackageSerializer,
    WishListDetailSerializer,
    WishListSerializer,
)


class WishListViewSet(
    ActionSerializerClassMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    action_serializer_class = {
        "retrieve": WishListDetailSerializer,
        "accept": WishListDetailSerializer,
        "reject": WishListDetailSerializer,
    }

    @atomic
    @extend_schema(request=None)
    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        wish_list = self.get_object()
        wish_list.set_status(WishListStatuses.ACCEPTED)
        Package.objects.create(wish_list=wish_list)
        return Response(self.get_serializer(wish_list).data)

    @atomic
    @extend_schema(request=None)
    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        wish_list = self.get_object()
        wish_list.set_status(WishListStatuses.REJECTED)
        return Response(self.get_serializer(wish_list).data)


class PackageViewSet(
    ActionSerializerClassMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    action_serializer_class = {
        "retrieve": PackageDetailSerializer,
        "send": PackageDetailSerializer,
    }

    @atomic
    @extend_schema(
        operation_id="packages_send",
        request=PackageSendBodySerializer,
    )
    @action(detail=True, methods=["post"])
    def send(self, request, pk=None):
        package = self.get_object()
        package.status = PackageStatuses.SENT
        package.save(update_fields=["status"])
        return Response(self.get_serializer(package).data)


class PackageDistributionViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Package.objects.all()
    serializer_class = PackageDistributionSerializer

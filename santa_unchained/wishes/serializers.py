import random

from rest_framework import serializers

from santa_unchained.wishes.constants import PackageSizes
from santa_unchained.wishes.models import Package, WishList, WishListItem


class WishListSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source="address.country")
    city = serializers.CharField(source="address.city")

    class Meta:
        model = WishList
        fields = ("id", "name", "kindness", "country", "city", "created_at")


class WishListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = ("id", "name")


class WishListDetailSerializer(WishListSerializer):
    country = serializers.CharField(source="address.country")
    city = serializers.CharField(source="address.city")
    post_code = serializers.CharField(source="address.post_code")
    address = serializers.SerializerMethodField()
    items = WishListItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = (
            "id",
            "age",
            "name",
            "kindness",
            "country",
            "city",
            "post_code",
            "address",
            "created_at",
            "items",
            "status",
        )

    def get_address(self, obj):
        return f"{obj.address.street} {obj.address.house_number}"


class PackageSendBodySerializer(serializers.Serializer):
    size = serializers.ChoiceField(PackageSizes.choices)


class PackageSerializer(serializers.ModelSerializer):
    wish_list_id = serializers.IntegerField(source="wish_list.id")
    name = serializers.CharField(source="wish_list.name")
    kindness = serializers.IntegerField(source="wish_list.kindness")
    country = serializers.CharField(source="wish_list.address.country")
    city = serializers.CharField(source="wish_list.address.city")

    class Meta:
        model = Package
        fields = (
            "id",
            "wish_list_id",
            "name",
            "kindness",
            "status",
            "country",
            "city",
            "created_at",
        )


class PackageDetailSerializer(PackageSerializer):
    age = serializers.IntegerField(source="wish_list.age")
    items = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    post_code = serializers.CharField(source="wish_list.address.post_code")

    class Meta:
        model = Package
        fields = (
            "wish_list_id",
            "name",
            "age",
            "kindness",
            "country",
            "city",
            "post_code",
            "address",
        ) + ("id", "items", "created_at", "status", "size")

    @staticmethod
    def get_items(obj):
        return WishListItemSerializer(obj.wish_list.items.all(), many=True).data

    @staticmethod
    def get_address(obj):
        return f"{obj.wish_list.address.street}, {obj.wish_list.address.house_number}"


class PackageDistributionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="wish_list.name")
    address = serializers.SerializerMethodField()
    postcode = serializers.CharField(source="wish_list.address.post_code")
    city = serializers.CharField(source="wish_list.address.city")
    country = serializers.CharField(source="wish_list.address.country")

    class Meta:
        model = Package
        fields = ("id", "name", "address", "postcode", "city", "country")

    def get_address(self, obj):
        return f"{obj.wish_list.address.street}, {obj.wish_list.address.house_number}"

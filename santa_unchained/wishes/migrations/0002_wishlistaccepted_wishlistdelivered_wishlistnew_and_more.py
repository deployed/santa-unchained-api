# Generated by Django 4.1.3 on 2022-11-30 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wishes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WishListAccepted",
            fields=[],
            options={
                "verbose_name": "accepted wish list",
                "verbose_name_plural": "accepted wish lists",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("wishes.wishlist",),
        ),
        migrations.CreateModel(
            name="WishListDelivered",
            fields=[],
            options={
                "verbose_name": "delivered wish list",
                "verbose_name_plural": "delivered wish lists",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("wishes.wishlist",),
        ),
        migrations.CreateModel(
            name="WishListNew",
            fields=[],
            options={
                "verbose_name": "new wish list",
                "verbose_name_plural": "new wish lists",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("wishes.wishlist",),
        ),
        migrations.CreateModel(
            name="WishListReadyForShipping",
            fields=[],
            options={
                "verbose_name": "wish list ready for shipping",
                "verbose_name_plural": "wish lists ready for shipping",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("wishes.wishlist",),
        ),
        migrations.CreateModel(
            name="WishListRejected",
            fields=[],
            options={
                "verbose_name": "rejected wish list",
                "verbose_name_plural": "rejected wish lists",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("wishes.wishlist",),
        ),
    ]

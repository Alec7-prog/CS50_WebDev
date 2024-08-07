# Generated by Django 5.0.7 on 2024-08-02 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listing_watchlist_delete_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auctions/static/auctions/images/'),
        ),
    ]

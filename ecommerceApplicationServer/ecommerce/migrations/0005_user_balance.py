# Generated by Django 4.0.2 on 2022-02-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_goods_sale_alter_goods_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, default='w240h240.jpg', null=True, upload_to=''),
        ),
    ]

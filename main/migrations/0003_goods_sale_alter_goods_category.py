# Generated by Django 4.1.4 on 2023-01-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.CharField(choices=[('Orange', 'Orange'), ('Blueberry', 'Blueberry'), ('Banana', 'Banana'), ('Apple', 'Apple'), ('Mango', 'Mango'), ('Strawberry', 'Strawberry')], max_length=30),
        ),
    ]

# Generated by Django 3.0.8 on 2020-11-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0007_auto_20201130_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronawars',
            name='image_1_big',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='coronawars',
            name='image_2_big',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='coronawars',
            name='image_3_big',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='coronawars',
            name='image_4_big',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='coronawars',
            name='image_5_big',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='coronawars',
            name='image_6_big',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]

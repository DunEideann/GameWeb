# Generated by Django 3.0.8 on 2020-11-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soulandspirit',
            name='image_1_big',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='soulandspirit',
            name='image_2_big',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='soulandspirit',
            name='image_3_big',
            field=models.ImageField(blank=True, help_text='Only necessary for models A y B', null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='soulandspirit',
            name='image_4_big',
            field=models.ImageField(blank=True, help_text='Only necessary for model B', null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='soulandspirit',
            name='image_5_big',
            field=models.ImageField(blank=True, help_text='Only necessary for models B y C', null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='soulandspirit',
            name='image_6_big',
            field=models.ImageField(blank=True, help_text='Only necessary for model C', null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='info_home',
            name='home_destination',
            field=models.CharField(choices=[('#top', 'Home'), ('#blog', 'News'), ('#featured', 'Developer Team'), ('#detailednews', 'Detailed News'), ('#projects', 'Soul&Spirit'), ('#projects2', 'CoronaWars'), ('#contact', 'Contact')], default='top', max_length=15),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-20 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lunchmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='filename',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='original_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1'),
        ),
        migrations.AddField(
            model_name='category',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2'),
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]

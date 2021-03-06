# Generated by Django 3.0.7 on 2020-06-12 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=40, verbose_name='会社名')),
                ('draw_number', models.CharField(max_length=100, verbose_name='図面番号')),
                ('material', models.CharField(max_length=40, verbose_name='材料')),
                ('material_size', models.CharField(max_length=40, verbose_name='材料サイズ')),
                ('outsourcing', models.CharField(blank=True, max_length=40, null=True, verbose_name='外注名')),
                ('outsourcing_content', models.CharField(blank=True, max_length=100, null=True, verbose_name='内容')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Draw',
            },
        ),
    ]

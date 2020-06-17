from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Draw(models.Model):
    '''図面登録モデル'''

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    customer = models.CharField(verbose_name='会社名', max_length=40)
    draw_number = models.CharField(verbose_name='図面番号', max_length=100)
    material = models.CharField(verbose_name='材料', max_length=40)
    material_size = models.CharField(verbose_name='材料サイズ', max_length=40)
    outsourcing = models.CharField(verbose_name='外注名', max_length=40, blank=True, null=True)
    outsourcing_content = models.CharField(verbose_name='内容', max_length=100, blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Draw'

    def __str__(self):
        return self.draw_number
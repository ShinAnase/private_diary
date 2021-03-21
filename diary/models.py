from django.db import models
from accounts.models import CustomUser

class Diary(models.Model):
    """日記モデル"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    #blank=Trueとnull=Trueのときに、対象が空であることを許容する。
    title = models.CharField(verbose_name='ユーザー', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    create_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True) #auto_now_add：レコード追加時に現在日を自動追記
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True) #auto_now：レコード更新時に現在日を自動追記

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title
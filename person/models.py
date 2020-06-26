from django.db import models

# Create your models here.


class Person(models.Model):
    ''' 玩家 '''
    # 玩家名称
    name = models.CharField(max_length=40)
    # 密码
    paassword = models.CharField(max_length=20)
    # 最大可装配卡牌
    maxCardNumbers = models.IntegerField(default=3)
    # 最大血量
    maxBloodValue = models.IntegerField(default=100)
    # 当前血量
    bloodValue = models.IntegerField(default=99)
    # 最大魔法
    maxMagicValue = models.IntegerField(default=100)
    # 当前魔法值
    magicValue = models.IntegerField(default=99)

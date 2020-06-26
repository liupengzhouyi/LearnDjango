from django.db import models

# Create your models here.

class Monster(models.Model):
    ''' 怪物 '''
    # 怪物名称
    name = models.CharField(max_length=40)
    # 最大可装配卡牌
    maxCardNumbers = models.IntegerField(default=4)
    # 最大血量
    maxBloodValue = models.IntegerField(default=1000)
    # 当前血量
    bloodValue = models.IntegerField(default=999)
    # 最大魔法
    maxMagicValue = models.IntegerField(default=1000)
    # 当前魔法值
    magicValue = models.IntegerField(default=998)
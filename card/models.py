from django.db import models

# Create your models here.

class Card(models.Model):
    ''' 卡牌类 '''
    # 卡牌名称
    name = models.CharField(max_length=40)
    # 技能名称
    funcName = models.CharField(max_length=40)
    # 消耗魔法值
    consume = models.IntegerField(default=10)
    # 技能描述
    func = models.CharField(max_length=100)
    # 回血值
    returnBloodValue = models.IntegerField()
    # 恢复魔法
    returnMagicValue = models.IntegerField()
    # 伤害
    damageValue = models.IntegerField()
    # 防护
    protect = models.IntegerField()
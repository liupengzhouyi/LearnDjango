from django.db import models
from card.models import Card
from person.models import Person
from monster.models import Monster
# Create your models here.


class CardRelitionship(models.Model):
    ''' 装备卡牌关系 '''
    # 对象
    type = models.CharField(max_length=10, default="玩家")
    # 玩家ID
    PersonId = models.IntegerField(default=1)
    # 怪物ID
    MonsterId = models.IntegerField(default=0)
    # 卡牌ID
    cardId = models.IntegerField()
    # 是否在装备
    using = models.IntegerField(default=0)


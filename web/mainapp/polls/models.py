"""docstring
    投票機能のモデルです
"""
from django.db import models


class Question(models.Model):
    """docstring
        質問についてのクラスです
    """
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """docstring
        質問を選択するクラスです
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

# Create your models here.
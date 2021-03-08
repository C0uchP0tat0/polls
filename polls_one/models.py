import datetime
from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Название опроса")
    start_date = models.DateField(verbose_name = "Дата публикации", default = datetime.datetime.now())
    end_date = models.DateField()
    description = models.CharField(max_length=100, verbose_name = "Описание")

    def __str__(self):
        return self.name

class Question(models.Model):
    question_id = models.ForeignKey(Poll,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name = "Вопрос")

    def __str__(self):
        return self.title

class Answer(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name = "Ответ")
     
    def __str__(self):
        return self.answer

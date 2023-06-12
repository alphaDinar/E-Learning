from django.db import models


class Grading(models.Model):
    grade = models.CharField(max_length=50)
    min_mark = models.IntegerField()
    max_mark = models.IntegerField()
    remark = models.CharField(max_length=100, null=True, blank=True)
    color_code = models.CharField(max_length=300, default='salmon')
    def __str__(self):
        return f'{self.grade} | {self.min_mark} - {self.max_mark}'
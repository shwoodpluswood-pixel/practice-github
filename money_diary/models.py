from django.db import models

class Income(models.Model):
    amount = models.IntegerField()
    source = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.source}: ¥{self.amount}"

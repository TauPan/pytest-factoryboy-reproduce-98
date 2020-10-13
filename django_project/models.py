from django.db import models


class Thing(models.Model):

    a = models.IntegerField(default=1)
    b = models.IntegerField(default=2)
    sum_ = models.IntegerField()

    def calculate_sum(self):
        self.sum_ = self.a + self.b
        self.save()

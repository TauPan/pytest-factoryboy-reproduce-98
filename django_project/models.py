from django.db import models


class Thing(models.Model):

    a = models.IntegerField(default=1)
    b = models.IntegerField(default=2)
    sum_ = models.IntegerField(null=True)

    def calculate_sum(self):
        print('Calculating: {} + {}.'.format(self.a, self.b))
        self.sum_ = self.a + self.b
        print('Sum: {}.'.format(self.sum_))
        self.save()

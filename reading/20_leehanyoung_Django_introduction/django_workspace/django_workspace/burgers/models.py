from django.db import models

class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Burger: ({self.name}, {self.price})>"

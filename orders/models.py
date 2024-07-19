from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    containers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.containers} containers"
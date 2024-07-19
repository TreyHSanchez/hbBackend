from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=100)
    review_text = models.TextField()

    def __str__(self):
        return self.username

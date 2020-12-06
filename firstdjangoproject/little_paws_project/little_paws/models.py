from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    def __str__(self):
        return self.question

# happy stories table
class Happystories(models.Model):
    description = models.CharField(max_length=500)
    happy_story = models.TextField()
    admin_verification = models.BooleanField(default=False)
    def __str__(self):
        return self.description
from django.db import models

# Create your models here.
class Organistaion_contact(models.Model):
    Organisation_name= models.CharField( max_length=200)
    Organisation_email=models.EmailField()
    Organisation_phone_number=models.BigIntegerField()
    Organisation_message=models.TextField()
    
    def __str__(self):
        return self.Organisation_name
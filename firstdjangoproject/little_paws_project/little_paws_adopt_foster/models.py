from django.db import models

# Create your models here.
#Registered cities  
class Registeredcities(models.Model):
    city_name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.city_name
#Registered shelters
class Registeredshelters(models.Model):
    shelter_name= models.CharField( max_length=200)
    shelter_city=models.ForeignKey(Registeredcities , on_delete=models.CASCADE)
    shelter_location=models.CharField( max_length=200)
    shelter_email=models.EmailField()
    shelter_contact_number=models.BigIntegerField()
       
    def __str__(self):
        return self.shelter_name
#Pet details
class Petdetails(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_image = models.ImageField(upload_to ='pics')
    
    pet_shelter_name = models.ForeignKey(Registeredshelters , on_delete=models.CASCADE)

    pet_type_choice=[('DOG','dog'),('CAT','cat')]
    pet_type=models.CharField(max_length=10, choices=pet_type_choice)

    gender_choice=[('MALE','male'),('FEMALE','female')]
    pet_gender = models.CharField(max_length=10, choices=gender_choice) 

    pet_breed = models.CharField(max_length=50) 
    pet_age=models.CharField(max_length=50)
    available_for_adoption = models.BooleanField(default=True)
    availabe_for_foster=models.BooleanField(default=True)
    last_modified=models. DateField(auto_now=True)
    def __str__(self):
        return self.pet_name
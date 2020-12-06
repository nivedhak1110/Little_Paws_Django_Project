from django.contrib import admin
from little_paws_adopt_foster.models  import Registeredshelters,Registeredcities,Petdetails
# Register your models here.
admin.site.register(Registeredshelters)
admin.site.register(Registeredcities)
admin.site.register(Petdetails)
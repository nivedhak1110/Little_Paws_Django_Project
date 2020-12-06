from django.shortcuts import render
from little_paws_adopt_foster.models import Registeredshelters,Registeredcities,Petdetails
from django.db.models import Q

# Create your views here.
#print adopt|foster cities
def adopt_foster_registered_cities_view(request):
    if request.method=='POST':
        print(request)
        search_query= request.POST['q']
        print(search_query)
        
        
        if search_query is not None :
            
            search_results =Registeredcities.objects.filter(Q(city_name__icontains=search_query))
            print(search_results)
            search_results_len = len(search_results)
            print(search_results_len)
            return render(request,"adopt_foster_city.html",{"cities":search_results  , "search_results_len":search_results_len})
        else:
            cities = Registeredcities.objects.all()
            return render(request, "adopt_foster_city.html" , {'cities':cities , 'search_results_len': 1 })
    else:
        cities = Registeredcities.objects.all()
        return render(request, "adopt_foster_city.html" , {"cities":cities,"search_results_len":1 })



#details of pets in the particular city
def pets_in_the_particular_city_view(request):
    if request.method == "POST":
        city= request.POST['city_name']
        print(city)
        cities=Registeredcities.objects.filter(city_name__icontains=city)
        city_ID=cities[0].pk
        print(city_ID)
        # to retrive the shelters in a particular city
        shelters_in_this_city=Registeredshelters.objects.filter(shelter_city=city_ID)
        #output is an array of shelters in this city
        pets_details_list=[]
        for shelter in shelters_in_this_city:  
            shelter_ID=shelter.pk
            #pets from the particular shelter
            pets_from_this_shelter=Petdetails.objects.filter(pet_shelter_name=shelter_ID)
            for pet in pets_from_this_shelter:
                pet_name=pet.pet_name
                pet_image = pet.pet_image
                pet_shelter_name=pet.pet_shelter_name
                pet_type=pet.pet_type
                pet_gender=pet.pet_gender
                pet_breed=pet.pet_breed
                pet_age=pet.pet_age
                available_for_adoption=pet.available_for_adoption
                print(available_for_adoption)
                availabe_for_foster=pet.availabe_for_foster
                print(available_for_adoption)
                last_modified=pet.last_modified
                pet_details = {
                            "pet_name":pet_name,
                            "pet_image":pet_image,
                            "pet_shelter":pet_shelter_name,
                            "pet_type":pet_type,
                            "pet_gender":pet_gender,
                            "pet_breed": pet_breed,
                            "pet_age":pet_age,
                            "available_for_adoption":available_for_adoption,
                            "availabe_for_foster":availabe_for_foster,
                            "last_modified":last_modified
                        }
                        
                print(pet_details)  
                pets_details_list.append(pet_details)   
                print(pets_details_list)   
                
        return render(request,"petdetails.html",{"pet_details":pets_details_list})
        
# shelter details view 
def shelter_details_view(request):
    if request.method=='POST':
        shelter_name=request.POST['shelter_details'] 
        print(shelter_name)
        shelter_details=Registeredshelters.objects.filter(shelter_name=shelter_name)
        print(shelter_details)
        return render(request,"shelter_details.html",{'shelter_details':shelter_details})

 
     
            
from django.shortcuts import render
from django.db.models import Q
from .models import Faq,Happystories
from django.contrib.postgres.search import SearchVector
# Create your views here.
# render home page
def home_page_view(request):
    return render(request,"Homepage.html")

# render adopt|foster|help page
def adopt_foster_help_view(request):
    return render(request, "adopt_foster_help.html")

# render help page
def help_view(request):
    return render(request, "help.html")

# render about page
def about_view(request):
    return render(request, "About.html")

# render FAQ page
def FAQ_view(request):
    if request.method=='POST':
        print(request)
        search_query= request.POST['q']
        print(search_query)
        submit_button=request.POST['submit']
        if search_query is not None :
            search_vector = SearchVector('question','answer')
            search_results = Faq.objects.annotate(search=search_vector).filter(search=search_query)
            print(search_results)
            search_results_len = len(search_results)
            print(search_results_len)
            return render(request,"FAQ.html",{"Faqs":search_results  , "search_results_len":search_results_len})
        else:
            Faqs = Faq.objects.all()
            return render(request, "FAQ.html" , {"Faqs":Faqs , "search_results_len": 1})
    else:
        Faqs = Faq.objects.all()
        return render(request, "FAQ.html" , {"Faqs":Faqs,"search_results_len":1 })

        
  #render happy stories page         
# render about page
def happy_stories_view(request):
    if request.method=='POST':
        print(request)
        description=request.POST['description']
        print(description)
        happy_story=request.POST['happy_story']
        
        a=Happystories(description=description,happy_story=happy_story,admin_verification=False)
        a.save()
        happy_stories = Happystories.objects.all()
        return render(request, "happystories.html", {"happystories":happy_stories})
    else:
        happy_stories = Happystories.objects.all()
        print(happy_stories)
        return render(request, "happystories.html" , {"happystories":happy_stories})

"""little_paws_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from little_paws.views import home_page_view , adopt_foster_help_view ,help_view,about_view,FAQ_view,happy_stories_view
from accounts.views import login_view,signup_view,contact_view,logout_view
from little_paws_adopt_foster.views import adopt_foster_registered_cities_view,pets_in_the_particular_city_view,shelter_details_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view , name = 'home'),
    path('adopt_Foster_help/', adopt_foster_help_view , name = 'adopt_foster_help'),
    path('adopt_Foster_help/help/', help_view ),
    path('help/', help_view , name = 'help'),
    path('about/', about_view , name = 'about'),
    path('login/', login_view , name="login"),
    path('logout/', logout_view , name="logout"),
    path('signup/', signup_view , name="signup"),
    path('contact/', contact_view , name="contact"),
    path('FAQ/', FAQ_view , name="FAQ"),
    path('happy_stories/', happy_stories_view , name="happy_stories_view"),
    #reset password
    path('login/reset_password/' , auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),

    path('reset_password_email_sent/' , auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),

    path('reset_password_confirmation/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),

    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    #adopt|foster registered cities
    path('adopt_foster_cities/',adopt_foster_registered_cities_view , name="adopt_foster_cities"),
    path('adopt_foster_cities/petdetails/',pets_in_the_particular_city_view, name='pets_in_the_particular_city' ),
    path('adopt_foster_cities/petdetails/shelter_details/',shelter_details_view, name='shelter_details')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
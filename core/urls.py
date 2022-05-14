from django.urls import path,include

urlpatterns = [
    path('',include('home.urls')),
    path('',include("register.urls"))
]

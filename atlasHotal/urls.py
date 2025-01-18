from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.Home.as_view()),
    path('about', views.about, name= 'about'),
    path('gallery', views.Galleryview.as_view(), name= 'gallery'),
    path('amenities', views.Amenitie.as_view(), name= 'amenities'),
    path('rooms', views.Roomview.as_view(), name= 'rooms'),
    path('contact', views.contactview.as_view(), name= 'contact'),
    path('roomDetail/<str:slug>', views.detail),
    path('mail', views.mailSendView , name= 'mail'),
]
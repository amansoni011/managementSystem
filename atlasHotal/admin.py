from django.contrib import admin
from .models import*
from django.utils.html import format_html 
# Register your models here.
admin.site.register(Offer)
admin.site.register(Amenities)
admin.site.register(Sayabout)
admin.site.register(Gallery)
admin.site.register(Galler_category)
admin.site.register(Room_type)
admin.site.register(Booking)
admin.site.register(Customer)

@admin.register(Room)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
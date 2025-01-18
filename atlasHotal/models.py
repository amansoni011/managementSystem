from django.db import models

# Create your models here.
from django.db import models

class Offer(models.Model):
    Offer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.FileField(blank=True,upload_to="gallery/")
    text = models.TextField()


    def __str__(self):
        return self.name
    
class Amenities(models.Model):
    Amenities_id = models.AutoField(primary_key=True)
    i_name = models.CharField(max_length=100)
    image = models.FileField(blank=True,upload_to="gallery/")


    def __str__(self):
        return self.i_name
    
class Sayabout(models.Model):
    Sayabout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    review = models.CharField(max_length=200)
    image = models.FileField(blank=True,upload_to="gallery/")
    # type = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    

class Galler_category(models.Model):
    Galler_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category


class Gallery(models.Model):
    Gallery_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Galler_category,on_delete=models.CASCADE,blank=True,null=True)
    image = models.FileField(blank=True,upload_to="galleery/")        

    def __str__(self):
        return self.category.category


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True,blank=True,null=True)
    update_at = models.DateTimeField(auto_now=True,blank=True,null=True) 
     
    def __str__(self):
        return self.name 
    
class Room_type(models.Model):
      Room_type_id = models.AutoField(primary_key=True)
      type = models.CharField(max_length=200)

      def __str__(self):
        return self.type

class Room(models.Model):
    Room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=222)       
    title = models.CharField(max_length=200)
    type = models.ForeignKey(Room_type,on_delete=models.CASCADE,blank=True,null=True)
    image = models.FileField(blank=True,upload_to="gallery/")
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True,blank=True,null=True)
    update_at = models.DateTimeField(auto_now=True,blank=True,null=True) 
     
    def __str__(self):
        return self.name

class Booking(models.Model):
    Booking_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    booking_date = models.CharField(max_length=100)
    check_in = models.DateField(blank=True,null=True)
    chack_out  = models.DateField(blank=True,null=True)
    tatal_amount = models.CharField(max_length=100)
    d_charge = models.CharField(max_length=500)
    is_checkout = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True,blank=True,null=True)
    update_at = models.DateTimeField(auto_now=True,blank=True,null=True) 
     

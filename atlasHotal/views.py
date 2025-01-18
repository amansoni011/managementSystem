from django.shortcuts import render,redirect
from django.views import View
# from .models import Offer,Amenities,Room,Sayabout
from .models import *
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail 
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.
# def home(request):
#     return render(request,'home.html')

#class for get data into model and return page(home.view)
class Home(View):
    template_name = 'home.html' 
     

    def get(self,request):
        data = Offer.objects.all()
        data2 = Amenities.objects.all()
        data3 = Room.objects.all()[:3]
        data4 = Sayabout.objects.all()
        return render(request, self.template_name,{'data':data,'data2':data2,'data3':data3,'data4':data4}) 

    
class Amenitie(View):
    template_name = 'amenities.html'

    def get(self,request):
        data2 = Amenities.objects.all()

        return render(request,self.template_name,{'data2':data2})   
       
def about(request):
    return render(request,'about_us.html')
    

# def rooms(request):
#     return render(request,'rooms.html')
class Roomview(View):
    template_name = 'rooms.html'

    def get(self,request):
        data3 = Room.objects.all()
        return render(request,self.template_name,{'data3':data3})

class contactview(View):
        template_name = 'contact.html'
        def get(self,request):
                return render(request,self.template_name)

        def post(self, request):
                print(request.POST)
                return JsonResponse({
                        "status": 200,
                        "title": "Good Job !!",
                        "message": "Your form is successfully submited."})

def detail(request,slug):
    data = Room.objects.get(slug=slug)
    return render(request,'detail.html',{'data':data})

# def gallery(request):
#     return render(request,'gallery.html')

class Galleryview(View):
     template_name = 'gallery.html'
     def get(self,request):
          data = Gallery.objects.all() 
          return render(request,self.template_name,{'data':data})


def mailSendView(request):
    if request.method == 'POST':
        name = "aman"
        # send_mail(
        #     "Test Mail From Django",
        #     f"<h1>Hello, {name}</h1>",
        #     "amansoniji326@gmail.com",
        #     ["chetanmalav9692@gmail.com"],
        #     fail_silently=False,
        # )
    
        context = {'name': request.POST.get('name'), 'room': request.POST.get('Room')}

        subject = "hello"
        from_email = "amansoniji326@gmail.com"
        # to = "chetanmalav9692@gmail.com"
        to = "suraj.juneco@gmail.com"
        text_content = "This is an important message."
        html_message = render_to_string('email_template.html', context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to, "rohitkrbxr11@gmail.com"])
        msg.attach_alternative(html_message, "text/html")
        msg.send()
        messages.success(request, "Successfully sent.")

        return redirect('/')




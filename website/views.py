from django.shortcuts import render
from django.core.mail import send_mail
from django.core import mail

# Create your views here.

def home(request):
    return render(request,'index.html',{})


def contact(request):
    if request.method =='POST':
        message_name =request.POST['message_name']
        message_email =request.POST['message_email']
        message =request.POST['message']

        #send an email
        send_mail(
            message_name,#SUBJECT
            message,#MESSAGE
            message_email,#FROM EMAIL
            ['tathagat.dalai@gmail.com'],#TO EMAIL

            )

        return render(request,'contact.html',{'message_name':message_name}) 
    else:
        return render(request,'contact.html',{})



def about(request):
    return render(request,'about.html',{})


def pricing(request):
    return render(request,'pricing.html',{})  


def service(request):
    return render(request,'service.html',{})



def appointment(request):
    if request.method =='POST':
        
        your_name =request.POST['your-name']
        your_phone =request.POST['your-phone']
        your_email =request.POST['your-email']
        your_address=request.POST['your-address']
        your_scheldule=request.POST['your-scheldule']
        your_time=request.POST['your-time']
        your_message=request.POST['your-message']
        appointment="Name : "+ your_name + "\n Phone : "+ your_phone +" \n Email : "+your_email  + "\n Address: "+ your_address +"\n scheldule : "+your_scheldule+"\n Day :"+your_time+"\n Message :"+your_message 
        #send an email
        send_mail(
            'Appointment Request View',#SUBJECT
            appointment,#MESSAGE
            your_email,#FROM EMAIL
            ['tathagat.dalai@gmail.com']#TO EMAIL

            )
    

        return render(request,'appointment.html',{
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_scheldule':your_scheldule,
            'your_time':your_time,
            'your_message':your_message




            
        }) 
    else:
        return render(request,'index.html',{})                      
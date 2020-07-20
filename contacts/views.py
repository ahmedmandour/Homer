from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(listing = listing,listing_id = listing_id , name = name , email = email, phone = phone , message = message)
       
        contact.save()

        messages.success(request,'sent successfully ,we will contact the realtor to call you ')

        return redirect('/listings/'+listing_id)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # Assuming 'home' is the name of your home page URL pattern
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

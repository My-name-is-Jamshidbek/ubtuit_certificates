from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Certificate, CertificateType


def home_view(request):
    # Assuming you have a Certificate model with a field named 'certificate_type'
    certificates = Certificate.objects.all()
    all_certificates_count = certificates.count()

    # Filter certificates based on selected certificate types
    selected_certificate_types = request.GET.getlist('certificate_type')
    if selected_certificate_types:
        certificates = certificates.filter(certificate_type__in=selected_certificate_types)

    # Retrieve all available certificate types to populate the template
    certificate_types = CertificateType.objects.all()

    # Number of certificates to display per page
    per_page = 5  # Adjust this number based on your preference

    # Create a Paginator instance
    paginator = Paginator(certificates, per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page', 1)

    try:
        # Get the Page object for the requested page
        certificates_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        certificates_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        certificates_page = paginator.page(paginator.num_pages)

    context = {
        "certificates": certificates_page,
        "certificate_types": certificate_types,
        "all_certificates_count": all_certificates_count,
    }

    return render(request, 'home.html', context=context)


def about_view(request):
    context = {
        "certificates": Certificate.objects.all(),
        "certificate_types": CertificateType.objects.all(),
    }

    return render(request, 'about.html', context=context)

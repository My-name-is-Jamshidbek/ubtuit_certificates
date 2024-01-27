from django.urls import path
from .views import home_view, about_view, certificate_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('certificate/<int:certificate_id>', certificate_view, name='certificate'),
]

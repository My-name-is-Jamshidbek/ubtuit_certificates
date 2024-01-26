from django.db import models


class CertificateType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.certificates.count()}"


class Certificate(models.Model):
    fullname = models.CharField(max_length=255)
    certificate_type = models.ForeignKey(CertificateType, related_name='certificates', on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='certificate_files/')  # Change 'certificate_files/' to your desired upload path
    image = models.ImageField(upload_to='certificate_images/', height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField(default=0, editable=False)
    image_width = models.PositiveIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


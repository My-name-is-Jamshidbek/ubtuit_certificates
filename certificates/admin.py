from django.contrib import admin
from .models import CertificateType, Certificate

@admin.register(CertificateType)
class CertificateTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'certificate_type', 'description', 'file', 'image', 'created_at', 'updated_at']
    list_filter = ['certificate_type']
    search_fields = ['fullname', 'description', 'file']
    readonly_fields = ['image_height', 'image_width', 'image_preview']

    def image_preview(self, obj):
        return obj.image_preview()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].widget.can_change_related = True
        return form

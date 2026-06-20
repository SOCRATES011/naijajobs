from django.contrib import admin
from .models import Job

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'category', 'job_type', 'is_active', 'date_posted', 'owner')
    list_filter = ('category', 'job_type', 'is_active', 'location')
    search_fields = ('title', 'company', 'location')
    actions = ['deactivate_listings']

    def deactivate_listings(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} listing(s) deactivated.")
    deactivate_listings.short_description = "Deactivate selected listings"

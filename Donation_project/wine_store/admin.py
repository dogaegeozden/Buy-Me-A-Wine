# LIBRARIES
from django.contrib import admin

# MODELS
from .models import (
    HomePageMetaDescription,
    HomePageHookLine, 
    Message,
)



# REGISTRATIONS

##############################

# HOME PAGE

##############################

@admin.register(HomePageMetaDescription)
class HomePageMetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

@admin.register(HomePageHookLine)
class HomePageHookLineAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hook Line', {
            'fields': ('text',)
        }),
    )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Message', {
            'fields': ('full_name', 'email', 'message', 'sending_time')
        }),
    )

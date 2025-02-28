from django.contrib import admin
from .models import CustomUser, Activity

# Register your models here.

class ActivityAdmin(admin.TabularInline):
    model = Activity
    extra = 2

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'created_at']
    inlines = [ActivityAdmin]
    
admin.site.register(CustomUser, UserAdmin)

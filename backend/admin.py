from django.contrib import admin
from backend.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

# Register your models here.

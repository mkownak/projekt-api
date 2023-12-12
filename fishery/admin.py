from django.contrib import admin
from . import models

# Register your models here.

class FisheryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "category",
        "latitude",
        "longitude",
        "date_added",
        "user_added",
        "status"
    )


admin.site.register(models.Fishery, FisheryAdmin)

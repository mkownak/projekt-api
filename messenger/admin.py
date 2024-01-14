from django.contrib import admin
from . import models

# Register your models here.


class MessegnerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sender",
        "reciver",
        "subject",
        'content',
        'date_sent'
    )


admin.site.register(models.Message, MessegnerAdmin)

from django.contrib import admin

# Register your models here.

from .models import Messages

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','time',)
    list_filter = ('time',)
    search_fields = ('name',)
    
 
    

admin.site.register(Messages, MessagesAdmin)
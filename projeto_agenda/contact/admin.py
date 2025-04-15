from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    search_fields = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('created_date',)
    list_per_page = 10
    list_max_show_all = 100
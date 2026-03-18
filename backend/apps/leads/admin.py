from django.contrib import admin
from .models import ContactMessage, QuoteRequest

admin.site.register(ContactMessage)
admin.site.register(QuoteRequest)
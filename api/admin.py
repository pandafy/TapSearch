from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    pass

@admin.register(Words)
class AdminWord(admin.ModelAdmin):
    pass

@admin.register(WordFrequencies)
class AdminWordFrequencies(admin.ModelAdmin):
    pass
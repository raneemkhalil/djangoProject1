from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from . import models

# Register your models here.
class Choices(admin.TabularInline):
    model = models.Choise
    fields = ['choice_text', 'vote', ]

class Questions(admin.ModelAdmin):
    list_display = ['question_text', 'date_published', ]
    inlines = [Choices, ]

admin.site.register(models.Question, Questions)

admin.site.register(models.Choise)
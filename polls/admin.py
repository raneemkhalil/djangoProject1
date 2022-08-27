from django.contrib import admin
from django.contrib.contenttypes import admin as ad
from .forms import QuestionsForm

from . import models
from fl_tags import models as md

# Register your models here.
class Tags(ad.GenericTabularInline):
    model = md.Tag
    fields = ['tag']
    extra = 1  # in my model always shows a 1 empty field.


class Choices(admin.TabularInline):
    model = models.Choice
    fields = ['choice_text', 'vote', ]


class QuestionChoices(admin.TabularInline):
    model = models.QuestionChoice
    extra = 1  # in my model always shows a 1 empty field.


class Questions(admin.ModelAdmin):
    list_display = ['question_text', 'date_published', ]
    inlines = [QuestionChoices, Tags]
    form = QuestionsForm


admin.site.register(models.Question, Questions)

admin.site.register(models.Choice)

admin.site.register(models.QuestionChoice)

admin.site.register(md.Tag)

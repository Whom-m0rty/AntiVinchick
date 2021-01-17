from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile_url')


@admin.register(User)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('peer_id', 'have_access')

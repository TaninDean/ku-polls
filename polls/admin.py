"""Class to make a display detail in admin config."""
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """Class to set mininum choice in admin config polls."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Class to config display detail in admin config polls."""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'end_date'],
                              'classes': ['collapse']})]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date',  'end_date', 'is_published')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

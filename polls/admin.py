from django.contrib import admin

from .models import Question, Choise


class ChoiceInLine(admin.TabularInline):
    model = Choise
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choise)
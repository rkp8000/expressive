from django.contrib import admin

from .models import Term, Sentence


class SentenceInline(admin.StackedInline):
    model = Sentence
    extra = 3


class TermAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['term_text', 'priority']}),
    ]
    inlines = [SentenceInline]


admin.site.register(Term, TermAdmin)

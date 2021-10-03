from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None,      {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']})
        ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

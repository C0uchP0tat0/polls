from django.contrib import admin
from .models import Poll, Question, Answer

class QuestionAdmin(admin.StackedInline):
    model = Question
    extra = 1
    
class PollAdmin(admin.ModelAdmin):
    fields = ['start_date', 'end_date', 'name', 'description']
    inlines = [QuestionAdmin]

admin.site.register(Poll, PollAdmin)
admin.site.register(Answer)




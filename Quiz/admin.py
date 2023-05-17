from django.contrib import admin
from .models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title','level','created_on')
    class Meta:
        model = Quiz

admin.site.register(Quiz, QuizAdmin)


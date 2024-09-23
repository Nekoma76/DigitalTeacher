from django.contrib import admin

from quizes.models import Category, Quiz, Question, Answer, UserAnswer

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('questionText',)}

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('answerText',)}
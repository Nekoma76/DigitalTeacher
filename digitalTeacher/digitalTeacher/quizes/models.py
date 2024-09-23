from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.CharField(blank=True, null=True, max_length=255)
    categories = models.ManyToManyField(Category, related_name='tests')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name=("questions"), on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    questionText = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.questionText}'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    answerText = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.answerText}'


class UserAnswer(models.Model):
    # user = models.ForeignKey(User, related_name=("results"), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

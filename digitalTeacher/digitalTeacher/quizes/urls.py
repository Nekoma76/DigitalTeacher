from django.urls import path

from quizes import views

app_name = 'quizes'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('quiz/<slug:quiz_slug>/', views.quiz, name='quiz')
]
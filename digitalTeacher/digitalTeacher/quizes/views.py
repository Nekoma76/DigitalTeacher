from audioop import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from quizes.models import Quiz, Answer, UserAnswer


# Create your views here.
def catalog(request):
    quizes = Quiz.objects.all()

    context = {
        "title": "Тесты",
        "quizes": quizes,
    }

    return render(request, 'quizes/catalog.html', context)


def quiz(request, quiz_slug):
    quiz = Quiz.objects.get(slug=quiz_slug)
    questions = quiz.questions.prefetch_related('answers')

    if request.method == 'POST':
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key

        correct_answers = 0

        # Цикл по вопросам для проверки правильности ответов
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, id=selected_answer_id)

                # Создание объекта UserAnswer с указанием всех необходимых полей
                user_answer = UserAnswer(
                    quiz=quiz,  # Указываем quiz
                    question=question,  # Указываем вопрос
                    selected_answer=selected_answer  # Указываем ответ
                )
                user_answer.save()  # Сохраняем объект UserAnswer в базе

                # Проверяем, правильный ли выбран ответ
                if selected_answer.is_correct:
                    correct_answers += 1

        # Рассчитываем результат
        total_questions = questions.count()
        percentage = (correct_answers / total_questions) * 100
        result = {
            'correct': correct_answers,
            'total': total_questions,
            'percentage': percentage,
        }

        # Передаем результат в контекст
        return render(request, 'quizes/quiz.html', {
            'quiz': quiz,
            'questions': questions,
            'result': result,  # передаем результаты теста
        })
    else:
        # Логика для отображения вопросов
        return render(request, 'quizes/quiz.html', {
            'quiz': quiz,
            'questions': questions,
            'result': None  # пока нет результата
        })
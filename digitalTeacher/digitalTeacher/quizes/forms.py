from django import forms

from quizes.models import UserAnswer


class QuizForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['question', 'answer']
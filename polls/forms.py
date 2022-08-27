from django import forms

from .models import Question, Choice


class QuestionsForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['choice', 'question_text', 'date_published']

    question_text = forms.CharField()
    date_published = forms.DateField()
    choice = forms.ModelMultipleChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.CheckboxSelectMultiple
        # widget=forms.SelectMultiple
        # widget=forms.Select
        # widget=forms.RadioSelect
    )

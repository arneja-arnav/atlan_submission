# views.py

from django.shortcuts import render, redirect
from django.views import View
from .models import Form, Question, Response, Answer
from .forms import ResponseForm

class FormView(View):
    template_name = 'form_template.html'

    def get(self, request, form_id):
        form = Form.objects.get(pk=form_id)
        questions = Question.objects.filter(form=form)
        return render(request, self.template_name, {'form': form, 'questions': questions})

    def post(self, request, form_id):
        form = Form.objects.get(pk=form_id)
        response = Response.objects.create(form=form, user_id=request.user.id if request.user.is_authenticated else None)
        questions = Question.objects.filter(form=form)

        for question in questions:
            answer_text = request.POST.get(f'question_{question.id}', '')
            Answer.objects.create(response=response, question=question, answer_text=answer_text)

        return redirect('success_page')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import *

# def simple_index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'new_try_app/simple_index.html', context)

class Simple_indexView(generic.ListView):
    template_name = 'new_try_app/simple_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'new_try_app/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'new_try_app/detail.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'new_try_app/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'new_try_app/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Question.DoesNotExist):
        return render(request, 'new_try_app/detail.html',
                      {'question': question, 'error_message': "You didn't selected your choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('new_try_app:results', args=(question.id,)))
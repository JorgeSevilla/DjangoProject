from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choise, Question

def index(resquest):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list,}
    return render(resquest, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/index.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return render(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question, 'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
    

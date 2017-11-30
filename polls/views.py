from django.shortcuts import render
from .models import Question

def index(resquest):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list,}
    return render(resquest, 'polls/index.html', context)


def detail(request, question_id):
    return render("You're looking at question % s" % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return render(response % question_id)

def vote(request, question_id):
    return render("You're voting on question %s." % question_id)

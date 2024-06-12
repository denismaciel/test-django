from django.http import HttpResponse

from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_questions}
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404
#     return render(request, "polls/detail.html", {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")

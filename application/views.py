from django.db import transaction, connection
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse
import json

from application.models import *

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'application/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'application/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'application/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'application/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app_urls:results', args=(question.id,)))

def mng(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'application/mng.html', context)

@transaction.atomic
def delete_question(request):
    if request.method == 'GET':
        qid = request.GET.get('question_id')
        question = get_object_or_404(Question, pk=qid)
        question.delete()

        for q in connection.queries:
            print(q)

        return HttpResponse(json.dumps({"message": "All ok with GET"}), content_type='application/json')

    elif request.method == "POST":
        qid = request.POST.get('question_id')
        question = get_object_or_404(Question, pk=qid)
        question.delete()

        return HttpResponse(json.dumps({"message": "All ok with POST"}), content_type='application/json')

    else:
        return HttpResponse(json.dumps({"message": "Unknown request method"}), content_type='application/json')

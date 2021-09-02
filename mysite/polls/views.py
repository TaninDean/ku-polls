from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Choice, Question

def index(request):
    latest_question_list = Question.object.order_by('-pub_date'[:5])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {question: question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

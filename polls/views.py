"""File to link url to page."""
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Vote
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    """Class to hendel when user what to go to index page."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return Question.object."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Class to hendel when user what to go to vote page."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Return Qestion pub_date."""
        return Question.objects.filter(pub_date__lte=timezone.now())

    def redirect(self):
        """Return index urls."""
        return HttpResponseRedirect(reverse('polls:index'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            try:
                vote = Vote.objects.get(user=user,
                                        choice__question=context["question"])
            except Vote.DoesNotExist:
                pass

        context["vote"] = vote
        return context


class ResultsView(generic.DetailView):
    """Class to hendel when user what to go to result page."""

    model = Question
    template_name = 'polls/results.html'

@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    """Return error when user submit the vote with out select choice."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        user = request.user
        vote = get_vote_for_user(user, question)
        if not vote:
            Vote.objects.create(user=user, choice=selected_choice)
        else:
            vote.choice = selected_choice
            vote.save()
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))

def get_vote_for_user(user, poll_question):
    """Find and return an existing vote for user in poll question.
    
    Return:
        The user's vote or None if no vote for this polls.
    """
    try: 
        votes = Vote.objects.filter(user=user).filter(choice__question=poll_question)
        if votes.count() == 0:
            return None
        else:
            return votes[0]
    except Vote.DoesNotExist:
        return None
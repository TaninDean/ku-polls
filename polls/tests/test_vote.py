import datetime
from polls.views import vote
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.test.client import RequestFactory
from polls.models import Question, Choice

def create_question(question_text, days):
    """Return Question."""
    time = timezone.now() + datetime.timedelta(days=days)
    time1 = timezone.now() + datetime.timedelta(days=days+7)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time,
                                   end_date=time1)


class VoteTest(TestCase):
    """Class for test vote."""

    def setUp(self):
        """Set up user."""
        self.re = RequestFactory()
        self.user = User.objects.create(username='tester', password='test')
        self.question = create_question('test', 0)
        Choice.objects.create(question=self.question, choice_text='testchoice')


    def test_vote(self):
        request = self.re.get('/polls/1/')
        request.user = self.user
        response = vote(request, '1')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """Remove all user"""
        User.objects.all().delete()
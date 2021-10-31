import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Question


def create_question(question_text, days):
    """Return Question."""
    time = timezone.now() + datetime.timedelta(days=days)
    time1 = timezone.now() + datetime.timedelta(days=days+7)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time,
                                   end_date=time1)


class QuestionDetailViewTests(TestCase):
    """Class to test question detail in detail page."""

    def test_future_question(self):
        """Test have questions in future."""
        future_question = create_question(
            question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """Test have question in past."""
        past_question = create_question(
            question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

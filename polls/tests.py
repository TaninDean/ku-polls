"""File to contain test of all fucntions in all class."""
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    """Test of Class Question."""

    def test_was_published_recently_with_future_question(self):
        """Test function was_published_recently when False."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """Test function was_published_recently when False."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """Test function was_published_recently when True."""
        time = timezone.now() - datetime.timedelta(hours=23,
                                                   minutes=59,
                                                   seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_is_published(self):
        """Test function is_published."""
        time = timezone.now() - datetime.timedelta(hours=23,
                                                   minutes=59,
                                                   seconds=59)
        end_time = timezone.now() + datetime.timedelta(hours=23,
                                                       minutes=59,
                                                       seconds=59)
        recent_question = Question(pub_date=time, end_date=end_time)
        self.assertIs(recent_question.is_published(), True)

    def test_can_vote(self):
        """Test function can_vote."""
        time = timezone.now() - datetime.timedelta(hours=23,
                                                   minutes=59,
                                                   seconds=59)
        end_time = timezone.now() + datetime.timedelta(hours=23,
                                                       minutes=59,
                                                       seconds=59)
        recent_question = Question(pub_date=time, end_date=end_time)
        self.assertIs(recent_question.can_vote(), True)


def create_question(question_text, days):
    """Return Question."""
    time = timezone.now() + datetime.timedelta(days=days)
    time1 = timezone.now() + datetime.timedelta(days=days+7)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time,
                                   end_date=time1)


class QuestionIndexViewTests(TestCase):
    """Class to test all functions in index."""

    def test_no_questions(self):
        """Test index is no question."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """Test have a question in past."""
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """Test have question published in future."""
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """Test have both past and future questions."""
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """Test have more than one questions in past."""
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


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

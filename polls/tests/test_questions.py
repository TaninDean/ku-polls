"""File to contain test of all fucntions in all class."""
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from polls.models import Question


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

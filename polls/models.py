"""File to contain function of each questions andchoice inquestions."""
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """Class to contain function of quesrions."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end published')

    def is_published(self):
        """Return is today is between pub_date and end_date."""
        now = timezone.now()
        return self.pub_date <= now < self.end_date

    def can_vote(self):
        """Return true if is_publish function is true."""
        if self.is_published():
            return True
        return False

    def was_published_recently(self):
        """Return is today is after pub_date."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    is_published.admin_order_field = 'pub_date'
    is_published.boolean = True
    is_published.short_description = 'Published recently?'

    def __str__(self):
        """Return text in question_text."""
        return self.question_text


class Choice(models.Model):
    """Class for contain text choice in each question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return choice_text in Choice."""
        return self.choice_text

    @property
    def votes(self): 
        count = Vote.objects.filter(choice=self).count()
        return count


class Vote(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote but {self.user.username} for {self.choice.choice_text}"

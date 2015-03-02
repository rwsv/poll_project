import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		future_question = Question(pub_date = timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		old_question = Question(pub_date = timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		recent_question = Question(pub_date = timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_question.was_published_recently(), True)
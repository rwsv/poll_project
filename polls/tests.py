import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		future_question = Question(pub_date = timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_question.was_published_recently(), False)

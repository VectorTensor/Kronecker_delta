from django.test import TestCase
from .models import Questions
# Create your tests here.
class QuestionTest(TestCase):
    @classmethod
    def questioninitial(cls):
        question=Questions.objects.Create(Question="hi",Answer="bye")
        question.save()


    def Tester(self):
        q= Questions.objects.get(id=1)

        Qes=f'{q.Question}'
        Ans=f'{q.Answer}'
        self.assertEqual(Qes,"hi")
        self.assertEqual(Ans,"bye")







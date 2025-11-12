from unittest import TestCase, main

from text_model import TextModel
text = "I want to start working as a programmer. I'm learning programming at Tel-Ran course.\
The teacher says to us that for becoming a programmer you should perform Homeworks.\
    But because of family and work I don't have time to do Homeworks"
class TestTextModel(TestCase):
    def setUp(self):
        self.textModel = TextModel(text)
    def test_two_answers_returned(self):
        expected = [
           'The teacher says to us that for becoming a programmer you should perform Homeworks',
            "But because of family and work I don't have time to do Homeworks"
        ]
        self.assertEqual(expected, self.textModel.getAnswers("Should you perform Homeworks",2))
    def test_one_answer_returned(self) :
        expected = [
           'The teacher says to us that for becoming a programmer you should perform Homeworks'
           
        ]
        self.assertEqual(expected, self.textModel.getAnswers("What should you perform",2)) 
    def test_no_answer_returned(self) :
       expected = [
        
        ]
       self.assertEqual(expected, self.textModel.getAnswers("What desturbs me achieve the purpose? ",2))       
        
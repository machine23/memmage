# from ..models import Tag, Question, Answer
import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestTag:
    def test_model(self):
        obj = mixer.blend('memcards.Tag')
        assert obj.pk == 1

    def test_str(self):
        tag = mixer.blend('memcards.Tag', name='tag_name')
        assert str(tag) == 'tag_name'


class TestQuestion:
    def test_model(self):
        obj = mixer.blend('memcards.Question')
        assert obj.pk == 1

    def test_str(self):
        test_string = 'test_question'
        question = mixer.blend('memcards.Question', text=test_string)
        assert str(question) == test_string


class TestAnswer:
    def test_model(self):
        obj = mixer.blend('memcards.Answer')
        assert obj.pk == 1

    def test_str(self):
        test_string = 'test answer'
        answer = mixer.blend('memcards.Answer', text=test_string)
        assert str(answer) == test_string

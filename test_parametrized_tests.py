"""
Organizing test and parametrizing
"""
# Parametrized tests: Run many tests in one
# pylint: disable=W0622
# pylint: disable=R0201
# pylint: disable=R0903
import pytest
from word_counter import count_words
class TestWordCounterParametrization:
    """
    In this case we want to test many tests in one function
    """
    Tests = [
        ("Today is Monday", 3),
        ("head", 1),
        ("He jumps", 2),
        ("He\nis\nnot\nfeeling\nwell", 5),
        ("Mein Hände", 2),
        ('<h1>This is a heading</h1>', 4),
        ('<h1 class="foo">this is a heading</h1>', 5),
        ("Joseph-Njeri", 2)
        ]
    @pytest.mark.parametrize('input, output', Tests)
    def test_all_in_one(self, input, output):
        """
        Testing all in one
        """
        assert count_words(input) == output

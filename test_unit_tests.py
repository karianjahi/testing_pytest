"""
Writing unit tests
"""
# Unit tests
# pylint: disable=R0201
# pylint: disable=R0903
# pylint: disable=W0622
import pytest
from word_counter import count_words
class TestWordCounter:
    """
    tests organized in class
    """
    def test_count_words(self):
        """
        We need to test the function count_words
        """
        text = "Today is Monday"
        assert count_words(text) == 3
    def test_single_word(self):
        """
        Single word test
        """
        text = "head"
        assert count_words(text) == 1
    def test_two_words(self):
        """
        test two words
        """
        text = "He jumps"
        assert count_words(text) == 2
    def test_linebreaks(self):
        """
        test for line breaks
        """
        text = "He\nis\nnot\nfeeling\nwell"
        assert count_words(text) == 5
    def test_accents(self):
        """
        Test accents
        """
        text = "Mein Hände"
        assert count_words(text) == 2
    def test_html(self):
        """
        test for html
        """
        text = '<h1>This is a heading</h1>'
        assert count_words(text) == 4
    def test_html_with_attributes(self):
        """
        test html with attributes
        """
        text = '<h1 class="foo">this is a heading</h1>'
        assert count_words(text) == 5
    def test_dashes(self):
        """
        test dashes
        """
        text = "Joseph-Njeri"
        assert count_words(text) == 2
class TestWordCounterExceptions:
    """
    Testing exceptions
    """
    def test_raise_type_error(self):
        """
        When text is not of type string
        """
        text = {"Ketan": "studies data science at spiced"}
        with pytest.raises(TypeError) as type_error:
            assert count_words(text) == 5
        assert "word counter accepts only strings" in str(type_error.value)
# Parametrized tests: Run many tests in one
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

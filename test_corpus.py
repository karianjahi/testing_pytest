"""
Testing the corpus.
Remember you don't have to import conftest.py
"""
from word_counter import count_words
def test_corpus(text_summary):
    """
    pytest for corpus
    """
    assert count_words(text_summary) == 15

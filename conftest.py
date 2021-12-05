"""
Creating a python module for test data and add a fixture decorator
"""
import pytest

TEXT_FILE = "data/some_corpus.txt"

@pytest.fixture
def text_summary():
    """
    Reading the file
    """
    with open(TEXT_FILE, "r") as file:
        return file.read()


# # - A class example
# class MyFixture:
#     """
#     Running a fixture in class
#     """
#     def read_file(self, file):
#         """
#         read file
#         """
#         with open(file, "r") as afile:
#             return afile.read()

# @pytest.fixture
# def text_summary():
#     """
#     Implement class
#     """
#     return MyFixture.read_file(TEXT_FILE)

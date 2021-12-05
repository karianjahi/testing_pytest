#!/bin/bash
coverage run -m pytest -s
coverage html
# pylint test.py

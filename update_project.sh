#!/bin/bash

# Rebuild the distribution
python3 setup.py sdist bdist_wheel

# Create a source distribution
python3 setup.py sdist

# Upload the distribution to PyPI
twine upload dist/*

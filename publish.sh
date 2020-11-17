#!/usr/bin/env bash

set -e

rm -rf build/ dist/

python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*

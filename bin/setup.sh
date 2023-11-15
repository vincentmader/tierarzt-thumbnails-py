#!/bin/sh

# Create new virtual environment for python, if not already done.
  [ -d ../.venv ] || python3 -m virtualenv ../.venv

# Install python dependencies.
  cd .. && ./.venv/bin/pip3 install -r requirements.txt

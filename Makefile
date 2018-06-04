.PHONY: stop prepare run

APP=miniURL
VENV_NAME=miniURL
VENV_ACTIVATE=.$(VENV_NAME)/bin/activate
PYTHON=$(VENV_NAME)/bin/python3

prepare: 
    python3 -m pip install virtualenv
    virtualenv $(APP)

venv:   $(VENV_NAME)/bin/activate

stop:   deactivate $(VENV_NAME)


run:    venv    $(PYTHON) main.py


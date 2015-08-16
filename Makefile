.PHONY: clean clean-pyc docs

COMMIT_HASH := $(shell git rev-parse --short --verify HEAD)
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
LIB_VERSION := $(shell python setup.py --version)
LIB_NAME := $(shell python setup.py --name)
SRC_DIRS := managers/ dumpers/ toolbox/ bin/ refreshers/ tests/
COVERAGE_VERSION := $(shell coverage --version 2>/dev/null)

help:
	@echo clean - clean up previous build
	@echo build - builds pyfsn project egg on dist/
	@echo install-all-deps - install all the project dependencies
	@echo help - show this help

compile:
	python -m compileall ${SRC_DIRS}

test: compile
	nosetests -v tests --with-coverage --cover-package=bin,toolbox --cover-branches

clean-pyc:
	find . -name \*.pyc -delete

clean: clean-pyc
	$(RM) -r build dist *.egg-info
	( cd dumpers; $(RM) -r build dist *.egg-info )

build-lib: clean
	python setup.py bdist_egg

build: clean
	python setupdeploy.py bdist_egg

install-all-deps:
	pip install -r requirements.txt -U
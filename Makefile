.PHONY: aa doc help install black build generatejs help tdd test setup
default:
	python -m pymake install
	python -m pymake black
	python -m pymake doc
	python -m pymake build
	python -m pymake generatejs
	python -m pymake test
	python -m pymake aa

aa: ## Make some aa (lava) to celebrate
	@echo '🌋 Success 🌋'

doc: ## Build docs
	python -m poetry run pydoc3 -w mything.api mything.domain mything.model mything.factory mything.feature mything builtins
	python -m poetry run pyreverse mything -SA -m y
	python ./scripts/pyapb.py  -w mything/apiblueprint.py --host https://mything.apiblueprint.org/
	python -c "from __future__ import print_function;print('moving generated files to docs/api/');import shutil;import os;files = os.listdir(); match = lambda file: file.endswith('.html') or file.endswith('.dot') or file.endswith('blueprint.md'); move = lambda file: (os.path.exists('docs/api/'+file) and os.remove('docs/api/'+file)) or shutil.move(file, 'docs/api/'); list(map(move,filter(match, files)))"

help: ## Show this help message.
	python -c "from __future__ import print_function;lines = list(open('Makefile')); match = lambda line: '##' in line; list(map(print,filter(match,lines)))"

setup: ## Install pyenv and poetry to home folder"
	bash ./scripts/pyenv-installer.sh
	python ./scripts/get-poetry.py
	pip install poetry

install: ## Install packages for project
	python -m poetry install

black: ## Format py files
	python -m poetry run black mything

build: ## Build pypi package
	python -m poetry build

generatejs: ## Build javascript
	python -m poetry run transcrypt -da -sf -de -m -n -b -ds -dc mything
	python -c "from __future__ import print_function;print('moving generated js to docs/api/js/');import shutil;import os;os.chdir('__target__');files = os.listdir(); match = lambda file: file.endswith('.js'); move = lambda file: (os.path.exists('../docs/api/js/'+file) and os.remove('../docs/api/js/'+file)) or shutil.move(file, '../docs/api/js/'); list(map(move,filter(match, files)))"

tdd: ## Run tests on file change
	python -m poetry run ptw

test: ## Run the tests
	python -m poetry run pytest
	python -m poetry run pytest --doctest-only mything


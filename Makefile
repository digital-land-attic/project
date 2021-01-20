BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
DOCS_DIR=./docs/

init:
	pip install -r requirements.txt

render:
	python3 render.py
	
clean::
	rm -rf $(DOCS_DIR)
	mkdir -p $(DOCS_DIR)
	
commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))

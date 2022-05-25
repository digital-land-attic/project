BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
DOCS_DIR=./docs/

render: updates render-pages copy-img
	
render-pages::
	mkdir -p docs
	python3 render.py

init:
	pip install -r requirements.txt

	
clean::
	rm -rf $(DOCS_DIR)
	mkdir -p $(DOCS_DIR)
	
commit-docs::
	git add docs
	git add projects
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))

copy-img::
	mkdir -p docs/images
	rsync -r src/images docs/

updates:
	python bin/update-project-pages.py

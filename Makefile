# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init:
	pip install --upgrade -r requirements.txt

render:
	mkdir -p docs
	python3 render.py

clobber:
	rm -rf docs

commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt project pages $(shell date +%F)"; git push origin $(BRANCH))
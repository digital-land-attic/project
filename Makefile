init:
	pip install -r requirements.txt

render:
	mkdir -p docs
	python3 render.py

clobber:
	rm -rf docs
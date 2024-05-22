.PHONY: clean build upload tag release rm-tag

VERSION=$(shell python setup.py --version)

clean:
	rm -rf build dist *.egg-info

build: clean
	pip install wheel
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

release: upload
	@echo "Released version $(VERSION)"

tag:
	git tag -a v$(VERSION) -m "Release version $(VERSION)"
	git push --tags

tag-force:
	git tag -f v$(VERSION) -m "Release version $(VERSION) remastered"
	git push -f origin v$(VERSION)

.PHONY: test
test:
	python -m unittest discover -s test

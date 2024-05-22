.PHONY: clean build upload tag release

VERSION=$(shell python setup.py --version)

clean:
	rm -rf build dist *.egg-info

build: clean
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

tag:
	git tag -a v$(VERSION) -m "Release version $(VERSION)"
	git push --tags

release: tag upload
	@echo "Released version $(VERSION)"


.PHONY: test
test:
	python -m unittest discover -s test

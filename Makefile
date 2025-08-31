.PHONY: all build-index generate-manifest generate-permalinks lint test clean

all: build-index generate-manifest generate-permalinks

build-index:
	python scripts/build_index.py

generate-manifest:
	python scripts/generate_manifest.py

generate-permalinks:
	python scripts/generate_readme_permalinks.py

lint:
	# Add linting commands here (e.g., ruff, black)

test:
	# Add testing commands here (e.g., pytest)

clean:
	rm -f index.jsonl
	rm -f EVIDENCE_MANIFEST.csv
	rm -f README_PERMALINKS.md
	rm -rf _text/
	rm -f *.log

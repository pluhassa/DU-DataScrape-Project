# DU-DataScrape-Project

## Prerequisites:
Install required tools:
```
pip install pylint pre-commit
```
Recommended one-time setup for git hooks:
```
pre-commit install
```

## Pylint:

This project uses **Pylint** to analyze and improve code quality, ensuring it is readable and follows industry practices. To run it:


### Running Pylint
To analyze your code, run:

```
pylint [insert file name].py
```

Pylint will output a report with errors, warnings, and suggestions. Each issue includes:
- **Line number** where the issue occurred
- **Error code** (e.g, C0114 for missing module docstring)
- **Description** of the issue

For example:
```
your_script.py:6:0: C0114: Missing module docstring(missing-module-docstring)
```

### Fixing Pylint Issues
If Pylint reports errors:
1. **Read the error description** to understand the issue
2. **Search for the error code** (e.g. "pylint C0114") to find solutions
3. **Update your code** to address the issue

## Command-Line Arguments with Argparse:

Arg Parse is a python module for parsing different command-line arguments, making it wasier to configure and run the script.

### How Argparse works
Argparse allows you to define:
- **Required arguments** (e.g., input/output files)
- **Optional arguments** (e.g., log level, platform)
- **Choices** (e.g., restrict values to specific options)

#### Example
```
python your_script.py --input "data.csv" --log-level "DEBUG"
```

| Argument | Description | Required | Choices | Default |
| -------- | -------- | -------- | -------- | -------- |
| --log-level | Set the logging level| No | DEBUG, INFO, WARNING, ERROR, CRITICAL | INFO |
| --file-path | Path to the input file | Yes | N/A | N/A |
| --platform | Select the platform to use | No | X, Youtube, Instagram | N/A |


## Unit Tests
Tests are located in `tests/tests_main.py`

Run test with disvoery:
```
python -m unittest discover -s tests -p "tests_*.py" -v
```

Current test coverage includes:
- Default argument behavior
- Valid argument behavior
- Invalid argparse choices raising SystemExit

## Pre-Upload Script

Before uploading, run `pre-uploads.ps1`:
```
powershell -ExecutionPolicy Bypass -File .\pre-upload.ps1
```
This script checks:
- Python availability
- pre-commit hooks
- pylint on `main.py`
- Default run of `main.py`
- unittest suite

## Notes on Pre-Commit Auto-Fixes
Some hooks can automatically modify files (for example, end-of-file-fixer). If that happens,
stage the changed files and run checks again:
```
git add .
pre-commit run --all-files
```

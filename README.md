# Zalo Integration SDK

This is a work in progress project. **Use at your own risk!**

At this point, this library only support Official Account APIs.

If you found any problems, please create an issue to track it, or feel free to open a PR.

## Installation

`pip install zalo_sdk`

## Build and Release

- Bump new version in setup.py
- Build and upload to pypi.org
```
python3 -m build
python3 -m twine upload dist/*
```

## Documentation

The code is its own document.

(I'm kidding, I'll add documentation later)

## Running the Test Cases
Before running the test cases, make sure to fill out all the required parameters in the test/base.py file
To run all the test cases, use the following command:
```
python run_tests.py
```
If you want to skip running a specific test case or a group of test cases, you can comment out the corresponding lines in the create_test_suite function.

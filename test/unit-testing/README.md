# Testing Folder - YOLO Model

This folder will be used for unit tests for the YOLOv8 model pipeline, including training, validation, and export functions. These tests ensure that the core functionality of the YOLO model is working as expected.

## Prerequisites

- Python 3.x
- The following Python libraries must be installed:
  - `ultralytics`
  - `torch`
  - `unittest` (installed by default with python)

## Executing the Tests
`python -m unittest discover -s tests -p "test_*.py"`
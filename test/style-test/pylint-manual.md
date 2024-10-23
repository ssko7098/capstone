# Pylint Manual

## Purpose

Pylint is a tool designed to:

- Check for **errors** in Python code.
- **Enforce coding standards** (such as PEP 8).
- Detect **code smells** and areas for improvement.
- Spot certain **type errors**.
- Provide **refactoring suggestions**.
- Offer insights into **code complexity**.

Using Pylint will help our team maintain high code quality and ensure alignment with the PEP 8 style guide.

---

## Steps to Use Pylint

### Step 1: Prepare Python Scripts

Pylint only works on `.py` files. Ensure all scripts are in the correct format:
- **Training scripts** written in Jupyter Notebooks (`.ipynb`) must be converted to Python (`.py`) files.
- **Model inference** and **post-processing** scripts, which are already in `.py` format, can be tested directly.

### Step 2: Install Pylint

Install Pylint by running the following command in your terminal:
```bash
pip install pylint
```

This will install Pylint and its dependencies.


### Step 3: Run Pylint
To run Pylint on a Python script, use the following command:
```bash
pylint path/to/your/script.py
```
Where `path/to/your/script.py` is the path to the Python script you want to check. Pylint will output a report with a score and suggestions for improvement.

### Step 4: Fix Errors and Warnings
Review the Pylint report and address any errors or warnings in your code. This may involve:
- **Correcting syntax errors**.
- **Refactoring code** for better readability.
- **Aligning with PEP 8 standards**.
- **Optimising code** for performance.

Repeat steps 3 and 4 until your code passes Pylint with a high score (above 9.0).
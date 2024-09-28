# First pylint test on 'train.py' in 'yolo-and-isc-manual.ipynb'

**Date:** Thursday 26 September 2024

**Time:** 10:30am

Results: 
************* 
Module train
train.py:36:0: C0304: Final newline missing(missing-final-newline)

train.py:1:0: C0114: Missing module docstring (missing-module-docstring)

train.py:3:0: E0401: Unable to import 'torch' (import-error)

train.py:4:0: E0401: Unable to import 'ultralytics' (import-error)

train.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)

train.py:9:22: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

train.py:9:22: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)

train.py:9:8: W0612: Unused variable 'output_file' (unused-variable)

-----------------------------------
Your code has been rated at 3.04/10

Action: 
After fixing the code manually and running Pylint again, the training script was able to get a 10/10 style rating. The fixed code was put onto the 'yolo-and-isc-manual.ipynb' file for team members to use.


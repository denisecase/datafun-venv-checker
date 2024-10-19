# DEVELOPER NOTES (NOT NEEDED FOR CHECKING)

Run locally to test. 
From a PowerShell terminal in the root project folder, run:

```shell
py datafun_venv_checker/venv_checker.py
```

Build this package and install locally to test.
From a PowerShell terminal in the root project folder, run:

```pwsh
py setup.py sdist bdist_wheel
py -m pip install -e .
```
# datafun-venv-checker

> Data Analytics Fundamentals: DataFun Venv Checker is a Python package that verifies that the project virtual environment has been created and activated in a local .venv folder.

It will also check whether the packages listed in a local requirements.txt have been installed into the local project virtual environment. 

## Features

- Verify if .venv exists
- Check if .venv is activated
- Ensure packages listed in requirements.txt are installed

## Installation

### Step 1. Add the Package

Add the following line to your local requirements.txt file to install this package:

```
git+https://github.com/denisecase/datafun_venv_checker.git#egg=datafun_venv_checker

```

### Step 2: Activate / Install / Run 

Create and activate your local project virtual environment in the .venv folder. 
Install (and upgrade) all packages in your requirements.txt.
Finally, run the checker to verify your setup.
More information is available in requirements.txt.


## Example Commands: Windows

Use a PowerShell terminal and run each command separately. 

```shell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade -r requirements.txt
check-venv
```

## Example Commands: Mac/Linux

Use zsh, bash, or PowerShell (pwsh) terminal and run each command separately.

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade -r requirements.txt
check-venv
```


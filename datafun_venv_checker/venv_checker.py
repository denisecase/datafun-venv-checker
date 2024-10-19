"""
venv_checker.py

This script provides a test suite for verifying the existence, activation, and correct package installation 
within a Python project's local virtual environment (.venv). 

The script performs the following checks:
- Ensures the .venv folder exists in the project root.
- Verifies that the .venv environment is activated.
- Checks if all the packages listed in the requirements.txt file are installed within the .venv.

Logs are generated and written to 'venv_checker.log', providing feedback on progress and results of each test.

Usage:
Run this script from the project root using the command for your operating system.
    py venv_checker.py
    python3 venv_checker.py
"""

# ====================================================
# Imports at the top
# ====================================================

import logging
import os
import subprocess
import sys
import unittest
from typing import List

# ====================================================
# Configure logging to send messages to console and a log file
# ====================================================

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create handlers: one for console and one for file output
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("venv_checker.log")

# Set format for both handlers
formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# ====================================================
# Declare global constants, variables, and functions
# ====================================================

RECOMMENDED_VENV_NAME: str = ".venv"
RECOMMENDED_REQUIREMENTS_FILE_NAME: str = "requirements.txt"

GUIDE_IF_DOT_VENV_MISSING: str = r"""
ERROR: Missing .venv folder - HOW TO FIX
    Create your local project virtual env and activate it.
    Open a terminal in your ROOT PROJECT FOLDER and run each command separately. 

    On Windows, use a PowerShell terminal.
       py -m venv .venv
       .\.venv\Scripts\activate
    On Mac or Linux, use your zsh or bash terminal. 
       python3 -m venv .venv
       source .venv/bin/activate
"""

GUIDE_IF_INACTIVE: str = r"""
ERROR: Local project virtual environment is not active - HOW TO FIX
    Create your local project virtual env and activate it.
    Open a terminal in your ROOT PROJECT FOLDER and run each command separately. 
    
    On Windows, use a PowerShell terminal.
       py -m venv .venv
       .\.venv\Scripts\activate
    On Mac/Linux, use your zsh or bash terminal. 
       python3 -m venv .venv
       source .venv/bin/activate

    If activation still fails, ensure you've installed a current Python version on your machine. 
"""
GUIDE_IF_REQ_FILE_MISSING: str = r"""
ERROR: Local requirements.txt file is missing - HOW TO FIX
    Create a requirements.txt file in your ROOT PROJECT FOLDER.
    
    On Windows, use a PowerShell terminal.
       ni requirements.txt
    On Mac or Linux, use your zsh or bash terminal. 
       touch requirements.txt

    Then, open your Project Folder in VS Code and edit the file. 
    List each required package, one per line, in requirements.txt.
"""

GUIDE_IF_REQ_PACKAGE_MISSING: str = r"""
ERROR: Not all packages listed in requirements.txt are installed - HOW TO FIX
    Install packages in requirements.txt into your active .venv. 
    Open a terminal in your ROOT PROJECT FOLDER and run the command.
    
    On Windows, use a PowerShell terminal.
       py -m pip install --upgrade -r requirements.txt
    On Mac/Linux, use your zsh or bash terminal. 
       python3 -m pip install --upgrade -r requirements.txt
"""

# Track overall progress (starts at 0%)
progress = 0


def log_progress():
    global progress
    if progress == 33:
        logging.info(f"Progress: {progress}% - You're 1/3 done - good start!")
    elif progress == 66:
        logging.info(f"Progress: {progress}% - You're 2/3 done - almost there!")
    elif progress == 100:
        logging.info(
            f"Progress: {progress}% - 100% completed - all checks passed. Nice work!"
        )
    else:
        logging.info(f"Progress: {progress}%.")


class TestLocalProjectVenv(unittest.TestCase):
    """
    Test suite to verify the existence, activation, and correct package installation
    in the .venv virtual environment without causing tests to fail if issues are found.
    """

    def setUp(self) -> None:
        """Set up the test by checking if requirements.txt exists."""
        self.requirements_file: str = RECOMMENDED_REQUIREMENTS_FILE_NAME

        if not os.path.isfile(self.requirements_file):
            logging.error(f"{self.requirements_file} file is missing.")
            self.skipTest(f"{self.requirements_file} file is missing.")

    def test_venv_exists(self) -> None:
        """
        Test that the .venv virtual environment folder exists in the project root.
        """
        global progress
        if not os.path.isdir(RECOMMENDED_VENV_NAME):
            logging.error(f"{RECOMMENDED_VENV_NAME} folder not found.")
            self.fail(f"Virtual environment ({RECOMMENDED_VENV_NAME}) not found.")
        else:
            progress += 33
            logging.info(f"{RECOMMENDED_VENV_NAME} folder exists.")
            log_progress()

    def test_venv_is_active(self) -> None:
        """
        Test that the virtual environment is active.
        """
        global progress
        if not os.getenv("VIRTUAL_ENV"):
            logging.error("Virtual environment is not active.")
            self.fail(
                f"Virtual environment is not active. Please activate {RECOMMENDED_VENV_NAME}."
            )
        else:
            progress += 33
            logging.info("Virtual environment is active.")
            log_progress()

    def test_requirements_installed(self) -> None:
        """
        Test that the packages listed in requirements.txt are installed in the virtual environment.
        """
        global progress
        if not os.path.isfile(self.requirements_file):
            logging.error(f"{self.requirements_file} is missing.")
            self.skipTest(
                f"{self.requirements_file} is missing, cannot verify installed packages."
            )
            return

        with open(self.requirements_file, "r") as f:
            # Filter out comment lines starting with '#'
            required_packages: List[str] = [
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith("#")
            ]

        missing_packages: List[str] = []
        for package in required_packages:
            try:
                # Check if the package is installed in the virtual environment
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "show", package],
                    stdout=subprocess.DEVNULL,
                )
                logging.info(f"Required {package} is installed.")
            except subprocess.CalledProcessError:
                missing_packages.append(package)

        if missing_packages:
            logging.error(f"Missing required packages: {', '.join(missing_packages)}")
            self.fail(
                f"Some packages from {self.requirements_file} are not installed in the virtual environment."
            )
        else:
            progress += 34  # Complete remaining 34%
            logging.info(f"All packages in {self.requirements_file} are installed.")
            log_progress()

    def fail(self, message: str) -> None:
        """
        Record failure and output message, but allow the test suite to continue.
        """
        logging.error(f"Test Failed: {message}")
        print(f"Test Failed: {message}")


if __name__ == "__main__":
    unittest.main(verbosity=0)

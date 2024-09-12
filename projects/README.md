# Array CLI Tool

## Project Description

The Array CLI Tool is an interactive command-line interface (CLI) tool written in Python that allows users to create and manipulate arrays. Users can generate arrays of random integers, sort them, and interact with the tool through a simple menu system.

This project also includes automated testing using pytest and is integrated with Jenkins for continuous integration. The tests are automatically triggered when changes are pushed to the GitHub repository.

## Features

- **Create Array**: Generate an array of random integers within a specified range.
- **Sort Array**: Sort an existing array in ascending order.
- **Interactive Menu**: Simple text-based interface for user interaction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Testing](#testing)
- [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/catwalk764/DSA_DataStructure-and-Algorithm-Python.git
   cd array_cli_tool
Set Up a Virtual Environment (Recommended)


python3 -m venv venv
source venv/bin/activate
Install Dependencies


pip install -r requirements.txt
Usage
Run the CLI Tool


python array_cli_tool.py
Follow the Menu Options to create an array, sort it, or exit.

Requirements
Python 3.6 or higher
pytest for running tests
You can install the required Python packages using:


pip install pytest
Testing
To run the tests, use the following command:


pytest test_array_cli_tool.py

License
This project is licensed under the MIT License - see the LICENSE file for details.

.gitignore
Include the following in your .gitignore file to avoid committing unnecessary files:


# Python
*.pyc
__pycache__/

# Virtual Environment
venv/

# Jenkins
*.log

# Pytest
.cache/
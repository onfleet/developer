# Task Import for Python

Uploads a CSV of tasks through the command line to the Onfleet API via Python

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Template File](#template-file)
- [Output](#output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```

git clone https://github.com/onfleet/developer.git


```
2. Install the required dependencies:

```

pip install onfleet


```

## Usage

1. Open the `import_template.csv` file and fill in the necessary data according to the provided template structure.

2. Replace `YOUR_API_KEY_HERE` with your actual Onfleet API key on line 15 of the program.

3. Run the program:

```

python task-import.py

```

4. Check the console output for any errors or warnings encountered during task creation.

5. Review the generated `warnings-{timestamp}.csv` file for a detailed list of warnings.

## Configuration

To configure the program, you need to provide your Onfleet API key. Replace `YOUR_API_KEY_HERE` on line 15 of the program with your actual API key. If needed, [here](https://support.onfleet.com/hc/en-us/articles/360045763292-API#h_01FTGN2E1AGNAA4DB3Q2RPVWD9) is more information on how to create an API key in Onfleet

## Template File

The template file (`import_template.csv`) should be filled out with the relevant data for creating tasks. Ensure that the data follows the provided template structure and includes all required information.

## Output

The program generates a `warnings-{timestamp}.csv` file that contains a list of rows with warnings encountered during task creation. Each row includes the original data from the template file and the corresponding warnings.

## Dependencies

The program relies on the following dependencies:

- `csv`: Python's built-in CSV module for reading and writing CSV files.
- `os`: Python's built-in module for interacting with the operating system.
- `warnings`: Python's built-in module for warning handling.
- `datetime`: Python's built-in module for working with dates and times.
- `onfleet`: Third-party library for interacting with the Onfleet API.

Make sure you have these dependencies installed before running the program.
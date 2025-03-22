# Delete Multiple Entities 

Delete Multiple Entities with a loop, this could be tasks or drivers, any allowed deletions.

## Table of Contents

- [Installation](#installation)
- [Disclaimer](#disclaimer)
- [Usage](#usage)
- [Configuration](#configuration)
- [Template File](#template-file)
- [Output](#output)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository:

```

git clone https://github.com/onfleet/developer.git


```
2. Install the required dependencies:

```

pip install requests
pip install datetime

```
## Disclaimer

This script does not have a roll back function. Any deletion using this script cannot be reversed. Please check before you execute this script. Onfleet is not responsible for any loss of data by using this script. 

## Usage

1. Open the `deletion.py` file and fill in the necessary line with your info.

2. Replace `ENTITY` with the entity you are accessing on line 6. Replace `USERNAME` with your actual Onfleet API Key on line 9. Include an array of Onfleet IDs you wish to delete  ``

3. Run the program:

```

python deletion.py

```

4. Check the console output for any errors encountered during deletion.

## Configuration

To configure the program, you need to provide your Onfleet API key. Replace `USERNAME` on line 9 of the program with your actual API key. If needed, [here](https://support.onfleet.com/hc/en-us/articles/360045763292-API#h_01FTGN2E1AGNAA4DB3Q2RPVWD9) is more information on how to create an API key in Onfleet

## Template File

## Output

ID that has been deleted or encountered any errors from the Onfleet API response.

## Dependencies

The program relies on the following dependencies:

- `requests`: Python's built-in module for simple HTTP requests.
- `datetime`: Python's built-in module for working with dates and times.


Make sure you have these dependencies installed before running the program.
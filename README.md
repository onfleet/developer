# Onfleet Developer open source repository

## Synopsis

This repository is a collection of resources and tools that may be freely used to augment and accelerate custom integration with the Onfleet API. 

**Note**  All python scripts require Python 3. 

## Content

* Onfleet webhooks backend - [python](https://github.com/onfleet/developer/tree/master/api-tools/webhooks)
  * Create dedicated endpoints to validate and receive payloads from various Onfleet webhook triggers.
* CSV task export - [python](https://github.com/onfleet/developer/tree/master/api-tools/export-tasks)
  * Export tasks from the [Onfleet list tasks API endpoint](https://docs.onfleet.com/reference#list-tasks) either in CSV format, or in plain JSON. Specify time range, task state, and other query parameters.
* Driver import - [python](https://github.com/onfleet/developer/tree/master/api-tools/driver_import)
  * Interactive CLI to bulk-import drivers from CSV-formatted spreadsheets via the Onfleet API.

## Related resources

[Onfleet API documentation](https://docs.onfleet.com/reference#introduction)

### Onfleet API Wrapper client libraries

* `pyonfleet` - Onfleet python API wrapper library:
  * [repository + documentation](https://github.com/onfleet/pyonfleet)
  * [PyPi project description](https://pypi.org/project/pyonfleet/)
* `node-onfleet` - Onfleet nodeJS API wrapper library:
  * [repository + documentation](https://github.com/onfleet/node-onfleet)
* `php-onfleet` - Onfleet PHP API wrapper library:
  * [repository + documentation](https://github.com/onfleet/php-onfleet)

## Installation

1  Clone the `developer` repository to your local development directory or download the zip file from github, and change to that directory.

```
git clone git@github.com:onfleet/developer ./onfleet-developer
cd ./onfleet-developer
```

2  Change directory to one of the onfleet/developer tools. Ex:

```
cd ./api-tools/webhooks
```

2a  (optional) create a new virtual environment that uses Python 3

```
python3 -m venv ./venv
```

2b  (optional) activate the virtual environment (note: venv must be activated in the terminal session before running any onfleet-developer python script)

```
source venv/bin/activate
```

3  Install all required python modules (note: use pip3 if python 3 isn't your default python version)

```
pip install -r requirements.txt
```

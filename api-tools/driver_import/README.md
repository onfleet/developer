# Onfleet Driver Import CLI
This is an interactive CLI that assist Onfleet admins to create new driver profiles in bulk.

## Usage
1. Download the code from the repository, ensure that you have all the required libraries listed in `requirements.txt` installed.
2. Make modifications to the file by inputting your own `Onfleet API key` and the `CSV filename` (`delimiters` can also be modified)
3. Execute the script to enter the CLI:
```
python driver_importer.py
```
4. Upon the prompt, use the arrow keys to select the team that you wish to import driver profiles to.
5. Option to select multiple teams here as the CLI prompts you to add more teams, simply click `Y` and select the teams until you are done.
6. Once the script completes, your results will be stored in a `result.csv` file for your reference.

> Note that all the valid drivers in the CSV file will be assigned to all the teams selected here.

## Import File Format
The imported file is of CSV format, and should have the following headers set assuming you are using comma as delimiters:
```
name,phone,capacity,displayName,vehicle type,vehicle description,vehicle licensePlate,vehicle color
```

Of all the parameters, `name` and `phone` are required, where all others are optional. The only exception is `team` which will be determined via the interactive CLI.
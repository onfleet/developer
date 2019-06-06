from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt

from onfleet import Onfleet
import csv
import os
import json
import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# User-defined parameters including API key and csv filename
api = Onfleet(api_key="<your_api_key>")
csv_file = "template.csv"
custom_delimiter = ","

file_name = os.path.join(THIS_FOLDER, csv_file)
# Styling for the CLI
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

def list_team():
    team_list = api.teams.get()
    team_name_list = []
    for team in team_list:
        team_name_list.append({"id": team["id"], "name": team["name"]})
    return team_name_list

def parse_worker(data_list, header_list, team_ids):
    driver_data = {}
    vehicle_data = {}
    for data in data_list:
        data_index = data_list.index(data)
        header = header_list[data_index]
        # Team IDs are pre-selected
        driver_data["teams"] = team_ids
        
        # Vehicle information are stored in a dict
        if (header.startswith("vehicle", 0, len(header))):
            vehicle_header = header.replace("vehicle ", "")
            vehicle_data[vehicle_header] = data
        else:
            driver_data[header] = data
        driver_data["vehicle"] = vehicle_data
    return driver_data

def write_result(result):
    with open("result.csv", mode="a") as result_file:
        employee_writer = csv.writer(result_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write error messages and request ID into the result file
        if ("request" in dir(result)):
            employee_writer.writerow([datetime.datetime.now(), result.status, result.message, result.request])
        # Write the successful import into the result file
        else:
            employee_writer.writerow([datetime.datetime.now(), 200, "worker " + result["name"] + " was created using the phone number of " + result["phone"]])

def create_worker(body):
    # Call the API wrapper to create a worker
    try:
        result = api.workers.create(body=body)
        write_result(result)
    except Exception as err:
        write_result(err)

def open_file_and_create_worker(file_name, team_ids):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=custom_delimiter)
        line_count = 0
        for row in csv_reader:
            # First row of the CSV file is always the headers
            if (line_count == 0):
                header_list = row
            else:
                data_list = row
                body = parse_worker(data_list, header_list, team_ids)
                create_worker(body)
            line_count += 1

def main():
    print("==== Welcome to the ∞ Onfleet Driver Importer ====")
    print("==================================================")
    print("You are currently importing", csv_file)
    # Storing the teams in a list
    team_list = list_team()
    choices = []
    team_ids_selected = []
    for team in team_list:
        choices.append(team["name"])

    # CLI loop
    while True:
        # Use the teams as our choices for the importer CLI
        questions = [
            {
                "type": "list",
                "name": "team",
                "message": "Please select the team that you want to import drivers to:",
                "choices": choices
            }
        ]
        # Prompt users to make a selection
        answers = prompt(questions, style=style)
        # Add team ID to the selected list
        for team in team_list:
            if (answers["team"] == team["name"]):
                team_ids_selected.append(team["id"])
        choices.remove(answers["team"])
        ask_again = [
            {
                "type": "confirm",
                "name": "repeat",
                "message": "Are there more teams to add?",
                "default": False
            }
        ]
        # Prompt users for multiple team addition
        repeat = prompt(ask_again, style=style)
        if repeat["repeat"] is False:
            break
    # Read the CSV and import workers
    open_file_and_create_worker(file_name, team_ids_selected)

    
if __name__ == "__main__":
    main()
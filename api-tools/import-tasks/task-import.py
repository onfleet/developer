import csv
import os
import warnings
import datetime
from onfleet import Onfleet
from onfleet.error import ValidationError

rowNumber = 1
warningsList = []
timeUploaded = str(datetime.datetime.now())

# Set the API endpoint URL

api = Onfleet(api_key="YOUR_API_KEY_HERE") # fill in your API key between the quotation marks
csv_file = "import_template.csv" #fill in the template file

def create_task(row):
    warning_title = ''
    # Parse the row and map the values to the task body
    task = {
        "Notification": row["Notification"],
        "Organization": row["Organization"],
        "Driver": row["Driver"],
        "Team": row["Team"],
        "Quantity": row["Quantity"],
        "Merchant": row["Merchant"],
        "ServiceTime": row["ServiceTime"],
        "notes": row["Task_Details"],
        "recipients": [
            {
                "name": row["Recipient_Name"],
                "phone": row["Recipient_Phone"],
                "notes": row["Recipient_Notes"]
            }
        ],
        "recipientName": row["Recipient_Name"]
        
    }
    lat = row["Latitude"].strip()
    lon = row["Longitude"].strip()


    # Check if the latitude and longitude values are not blank
    if lat and lon:
        task["destination"] = {
            "address": {
                "street": row["Address_Line1"],
                "city": row["City/Town"],
                "state": row["State/Province"],
                "postalCode": row["Postal_Code"],
                "country": row["Country"]
                },
            "location": {
                "coordinates": [
                    float(lat),
                    float(lon)
                ],
            
            }
        }

    else:
        task["destination"] = {
            "address": {
                "unparsed": row["Address_Line1"] + ", " + row["City/Town"] + ", " + row["State/Province"] + ", " + row["Postal_Code"] + ", " + row["Country"]
                },
        }

    # Check if the "completeAfter" cell is empty
    if row["completeAfter"]:
        task["completeAfter"] = row["completeAfter"]
    
    # Check if the "completeBefore" cell is empty
    if row["completeBefore"]:
        task["completeBefore"] = row["completeBefore"]

   # Call the Onfleet API to create a task
    
    try:
        response = api.tasks.create(body=task)
        warning_title = response.get("destination", {}).get("warnings", [])
        if warning_title:
            print(row["Address_Line1"], f"on row {rowNumber} has a warning: {warning_title}")
            # Add the warning to the row
            warningsList.append(row)
        return response
    except Exception as err:
        errMsg = str(err).split(',')[-1].strip("'")
        print (f"Error creating task on row {rowNumber}:", errMsg[:-1])
    

# Open the template file

custom_delimiter = ","
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

file_name = os.path.join(THIS_FOLDER, csv_file)

with open(file_name, "r") as template_file:
    # Read the template file as a CSV
    template_reader = csv.DictReader(template_file)
    # Add Task_ID to fieldnames
    fieldnames = template_reader.fieldnames + ["Task_ID"]  
    
    # Iterate through each row in the template
    for row in template_reader:
        rowNumber += 1
        try:
            # Create a task using the row
            response = create_task(row)
            # Check if the task has warnings
            if (bool(response['destination']['warnings'])):
                # Append the row to the warnings list
                row["warnings"] = (response['destination']['warnings'])
                # warningsList.append(row)


        except Exception as e:
            continue

     

# Write the warnings list to a separate CSV
with open("warnings" + timeUploaded + ".csv", "w") as warning_file:
    writer = csv.DictWriter(warning_file, fieldnames=template_reader.fieldnames + ["warnings"])
    writer.writeheader()
    for row in warningsList:
        writer.writerow(row)
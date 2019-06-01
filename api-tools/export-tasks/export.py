import csv
import json
import sys
import logging
from time import time
from onfleet import Onfleet

## USER DEFINED TASK EXPORT PARAMETERS

# Enter your API key below
API_KEY = ''

CSV_OUTPUT = True
STATE = "0,1,2,3"

# set from & to parameters in unix (ms)
FROM_DAYS_AGO = 300
TO_DAYS_AGO = 0

EXPORT_DIRECTORY = "./"
EXPORT_FILE_NAME = "export-%d" % int(time())

# set logging level and print to screen
# change level to logging.WARNING to suppress info logging messages
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

## END USER DEFINED TASK EXPORT PARAMETERS

api = Onfleet(api_key=API_KEY)

# convert times to UNIX timestamps with millisecond precision
FROM_TIME = str(int(time()-(FROM_DAYS_AGO*24*60*60)) * 1000)
TO_TIME = str(int(time()-(TO_DAYS_AGO*24*60*60)) * 1000)

def getTasksInRange(lastTaskId = None):
  params = {"from":FROM_TIME,"to":TO_TIME,"state":STATE,"lastId":lastTaskId}
  response = api.tasks.get(queryParams=params)
  return response

response = getTasksInRange()

tasks = None
tasks_fetched = 0
if 'tasks' in response:
  tasks = response['tasks']
  tasks_fetched += len(tasks)
  info = 'Fetched ' + str(tasks_fetched) + ' tasks'
  logging.log(logging.INFO, info)

# paginate if necessary
while 'lastId' in response:
  lastId = response['lastId']
  response = getTasksInRange(response['lastId'])
  tasks.extend(response['tasks'])
  tasks_fetched += len(response['tasks'])
  info = 'Fetched ' + str(tasks_fetched) + ' tasks'
  logging.log(logging.INFO, info)

if tasks and CSV_OUTPUT:
  # get keys for all tasks for column headers
  all_keys_set = set()
  all_keys_list = []
  for t in tasks:
    for k in t.keys():
      if not k in all_keys_set:
        all_keys_set.add(k)
        all_keys_list.append(k)

  # format data for CSV
  rows = []
  for t in tasks:
    row = []
    for k in all_keys_list:
      if k in t.keys():
        row.append(str(t[k]))
      else:
        row.append("")
    rows.append(row)

  # write to CSV
  csv_file = EXPORT_DIRECTORY + EXPORT_FILE_NAME + ".csv"
  with open(csv_file, 'w') as export_file:
    csvwriter = csv.writer(export_file)
    csvwriter.writerow(all_keys_list)

    for row in rows:
      try:
        csvwriter.writerow(row)
      except Exception as e:
        warning = "skipped:", e
        logging.log(logging.WARNING, warning)
        pass
  info = 'Export file created: ' + csv_file
  logging.log(logging.INFO, info)

elif tasks and not CSV_OUTPUT:
  # write JSON line response to file
  json_file = EXPORT_DIRECTORY + EXPORT_FILE_NAME + ".jsonl"
  with open(json_file, 'w') as export_file:
    for t in tasks:
      try:
        export_file.write(str(json.dumps(t)) + "\n")
      except Exception as e:
        logging.exception(e, "\n", json.dumps(t))
        raise
  info = 'Export file created: ' + json_file
  logging.log(logging.INFO, info)

else:
  warning = "No tasks returned in this period"
  logging.log(logging.WARNING, warning)
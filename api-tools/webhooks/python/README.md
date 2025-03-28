## Synopsis

Endpoints for each Onfleet webhook trigger. Validate the webhook and print payload to screen

## Installation

### WARNING
This project is incompatible with python versions later than 3.6.15. 
If you are using a later version of python, please use [pyenv](https://github.com/pyenv/pyenv) or another tool to manage versions of python on your system. 

1. ```pip install -r requirements.txt```
2. ```export FLASK_APP=testwebhooks.py; flask run```
3. expose to the wider internet ( if using ngrok: start ngrok server ) 
4. Create a webhook for your trigger event, using the path from the table below as your webhook URL.

 Event | path 
 ------|-------
 Task started |   /taskstart
 Driver ETA less than or equal to |   /taskETA
 Driver arriving, at or closer than |   /taskarrival
 Task completed |   /taskcomplete
 Task failed |   /taskfailed
 Driver status changed |   /workerduty
 New task created |   /taskcreated
 Task updated |   /taskupdated
 Task deleted |   /taskdeleted
 Task assigned |   /taskassigned
 Task unassigned |   /taskunassigned
 Task delay time is greater than or equal to |   /taskdelayed
 SMS Recipient Response Missed |   /smsrecipientresponsemissed
 Task Cloned |   /taskcloned

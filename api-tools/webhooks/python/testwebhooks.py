from flask import Flask, request, make_response
import os
import json
app = Flask(__name__)

# trigger id 0
@app.route('/taskstart', methods=['GET','POST'])
def taskstart():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task start')
    print(json.dumps(request.get_json()))
   # warn_if_unverified(request)
    return ('',200)

# trigger id 1
@app.route('/taskETA', methods=['GET','POST'])
def tasketa():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task ETA')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 2
@app.route('/taskarrival', methods=['GET','POST'])
def taskarrival():
  # validate only
  if request.method == 'GET':
    print(request.args.get('check',''))
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task arrival')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 3
@app.route('/taskcomplete', methods=['GET','POST'])
def taskcomplete():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task complete')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 4
@app.route('/taskfailed', methods=['GET','POST'])
def taskfailed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task failed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 5
@app.route('/workerduty', methods=['GET','POST'])
def workerduty():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('worker duty')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 6
@app.route('/taskcreated', methods=['GET','POST'])
def taskcreated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task created')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 7
@app.route('/taskupdated', methods=['GET','POST'])
def taskupdated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task updated')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 8
@app.route('/taskdeleted', methods=['GET','POST'])
def taskdeleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task deleted')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 9
@app.route('/taskassigned', methods=['GET','POST'])
def taskassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task assigned')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 10
@app.route('/taskunassigned', methods=['GET','POST'])
def taskunassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task unassigned')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 12
@app.route('/taskdelayed', methods=['GET','POST'])
def taskdelayed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task delayed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 13
@app.route('/taskcloned', methods=['GET','POST'])
def taskcloned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task cloned')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 14
@app.route('/smsrecipientresponsemissed', methods=['GET','POST'])
def smsrecipientresponsemissed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('SMS recipient response missed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 15
@app.route('/workercreated', methods=['GET','POST'])
def workercreated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print(' Worker Created')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 16
@app.route('/workerdeleted', methods=['GET','POST'])
def workerdeleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('Worker Deleted')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)

# trigger id 17
@app.route('/smsrecipientoptout', methods=['GET','POST'])
def smsrecipientoptout():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('SMS Recipient Opt Out')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)   

# trigger id 18
@app.route('/autodispatchjobcompleted', methods=['GET','POST'])
def autodispatchjobcompleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('auto Dispatch Job Completed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200)   

# trigger id 19
@app.route('/taskbatchcreatejobcompleted', methods=['GET','POST'])
def taskbatchcreatejobcompleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task batch create job completed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 20
@app.route('/routeoptimizationjobcompleted', methods=['GET','POST'])
def routeOptimizationjobcompleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Optimization Job Completed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 21
@app.route('/routeplancreated', methods=['GET','POST'])
def routeplancreated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Created')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 22
@app.route('/routeplanstarted', methods=['GET','POST'])
def routeplanstarted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Started')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 23
@app.route('/routeplancompleted', methods=['GET','POST'])
def routeplancompleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Completed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 24
@app.route('/workerupdated', methods=['GET','POST'])
def workerupdated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('worker Updated')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 25
@app.route('/routeplanupdated', methods=['GET','POST'])
def routeplanupdated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route plan updated')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 26
@app.route('/routeplanunassigned', methods=['GET','POST'])
def routeplanunassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Unassigned')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 27
@app.route('/routeplanassigned', methods=['GET','POST'])
def routeplanassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Assigned')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 28
@app.route('/routeplandelayed', methods=['GET','POST'])
def routeplandelayed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('route Plan Delayed')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

# trigger id 29
@app.route('/predictedtaskdelay', methods=['GET','POST'])
def predictedtaskdelay():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('predicted Task Delay')
    print(json.dumps(request.get_json()))
    #warn_if_unverified(request)
    return ('',200) 

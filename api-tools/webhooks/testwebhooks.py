from flask import Flask, request, make_response
import json
app = Flask(__name__)

@app.route('/taskstart', methods=['GET','POST'])
def taskstart():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task start')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskcomplete', methods=['GET','POST'])
def taskcomplete():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task complete')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/workerduty', methods=['GET','POST'])
def workerduty():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('worker duty')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskfailed', methods=['GET','POST'])
def taskfailed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task failed')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskupdated', methods=['GET','POST'])
def taskupdated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task updated')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskcreated', methods=['GET','POST'])
def taskcreated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task created')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskdeleted', methods=['GET','POST'])
def taskdeleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task deleted')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskdelayed', methods=['GET','POST'])
def taskdelayed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task delayed')
    print(json.dumps(request.get_json()))
    return ('',200)

@app.route('/taskETA', methods=['GET','POST'])
def tasketa():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('ETA threshold exceeded for task')
    print(json.dumps(request.get_json()))
    return ('',200)
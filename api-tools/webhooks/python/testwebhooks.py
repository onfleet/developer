from flask import Flask, request, make_response
import os
import json
app = Flask(__name__)

def verify_webhook(header, body, secret):
    """Verifies that the webhook originated from Onfleet.
    Args: 
        header: value of the X-Onfleet-Signature header in raw bytes
        body: should be the full body of the POST request in raw bytes, *not* the parsed JSON object
        secret: the value of the webhook secret from the Onfleet dashboard, in hexadecimal format
    Returns:
        True for verified, False for not verified"""
    import hashlib, hmac, binascii
    return hmac.new(binascii.a2b_hex(secret), body, 'sha512').hexdigest() == header

def warn_if_unverified(req):
  if app.secret and not verify_webhook(req.headers['X-Onfleet-Signature'], req.data, app.secret):
        print("Warning: could not verify the origin of the webhook invocation with provided secret key.")

@app.before_first_request
def check_for_secret():
  if "WEBHOOK_SECRET" in os.environ:
    app.secret = os.environ["WEBHOOK_SECRET"]
  else:
    print("\n***  NOTICE: Webhooks are running in unverified mode.  ***")
    print("To verify webhooks, copy your Webhook secret key from the Onfleet dashboard "
    "and set it in the environment as WEBHOOK_SECRET before running this script.\n\n"
    "For example, export FLASK_APP=testwebhooks.py WEBHOOK_SECRET=XXXXXXXXXXXXXXXXXXXXX flask run")
    app.secret = None

# trigger id 0
@app.route('/taskstart', methods=['GET','POST'])
def taskstart():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task start')
    print(json.dumps(request.get_json()))
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
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
    warn_if_unverified(request)
    return ('',200)
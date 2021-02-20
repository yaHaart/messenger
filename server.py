from flask import Flask, request, abort
import datetime
import time

app = Flask(__name__)

db = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Привет всем!'
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Привет, Jack!'
    }
]


@app.route("/")
def hello():
    return {'status': 'ok', 'name': 'haart messenger', 'date_time': datetime.datetime.now()}


@app.route("/status")
def status():
    return {'status': 'ok', 'name': 'haart messenger', 'date_time': datetime.datetime.now()}


@app.route("/send", methods=['POST'])
def send_message():
   data = request.json

   if not isinstance(data, dict):
       return abort(400)

   if 'name' not in data or 'text' not in data:
       return abort(400)

   name = data['name']
   text = data['text']

   if not isinstance(name, str) or not isinstance(text, str) or name == '' or text == '':
       return abort(400)


   message = {
       'time': time.time(),
       'name': name,
       'text': text
   }
   db.append(message)
   return {'ok': True}


@app.route("/messages")
def get_message():
    # after = 0

    try:
        after = float(request.args['after'])
    except:
        return abort(400)


    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break

    return {'messages': result}


app.run()

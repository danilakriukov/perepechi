from flask import Flask, Response, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis('localhost', port=6379, decode_responses=True)


def event_stream():
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('biden')

    for message in pubsub.listen():
        if message['data'] == 'Action':
            yield 'I am painting!\n\n'


@app.route("/")
def get_command():
    return Response(event_stream(), mimetype="text/plain")


@app.route("/joystick", methods=['GET', 'POST'])
def send_command():
    if request.method == 'POST':
       action = request.form['action']
       r.publish('biden', f'{action}')

    return render_template('joystick.html')


if __name__ == "__main__":
    app.run(debug = True)

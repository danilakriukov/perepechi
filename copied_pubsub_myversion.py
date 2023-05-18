#!/usr/bin/env python
import datetime
import flask
import redis


app = flask.Flask(__name__)
app.secret_key = 'asdf'
red = redis.StrictRedis()


def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        print ("pubsub.message: " + str(message['data']))
        #if message['type']=='message':
        if (message['data'] == b'Action'):
            print ("pubsub.message: " + str(message['data']))
            yield 'data: %s\n\n' % message['data'].decode('utf-8')
        elif (message['data'] == b'Stop'):
            print ("pubsub.message: " + str(message['data']))
            yield 'data: %s\n\n' % message['data'].decode('utf-8')


@app.route('/post', methods=['POST'])
def post():
    #message = flask.request.form['action']
    message = 'Action'
    #user = flask.session.get('user', 'anonymous')
    #now = datetime.datetime.now().replace(microsecond=0).time()
    #red.publish('chat', u'[%s] %s: %s' % (now.isoformat(), user, message))
    red.publish('chat', message)
    return flask.Response(status=204)

@app.route('/stop', methods=['POST'])
def stop():
    #message = flask.request.form['action']
    message = 'Stop'
    #user = flask.session.get('user', 'anonymous')
    #now = datetime.datetime.now().replace(microsecond=0).time()
    #red.publish('chat', u'[%s] %s: %s' % (now.isoformat(), user, message))
    red.publish('chat', message)
    return flask.Response(status=204)


@app.route('/stream')
def stream():
    return flask.Response(event_stream(),mimetype="text/event-stream")


@app.route('/')
def game():
    return """
        <!doctype html>
        <title>chat</title>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <style>body { max-width: 500px; margin: auto; padding: 1em; background: black; color: #fff; font: 16px/1.6 menlo, monospace; }</style>
        <pre id="out"></pre>
        <script>
            function sse() {
                var source = new EventSource('/stream');
                var out = document.getElementById('out');
                source.onmessage = function(e) {
                    // XSS in chat is fun (let's prevent that)
                    //out.textContent =  'rabotnik draws!' + '\\n' + out.textContent;
                    out.textContent = 'malyar goes right!' + e.data + '\\n' + out.textContent;
                };
            }
            sse();
        </script>
    """

@app.route('/joystick')
def joystick():
    return """
        <!doctype html>
        <title>chat</title>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <button onmousedown="vPravo()" onmouseup="stop()">Вправо</button>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/1.2.2/axios.min.js" integrity="sha512-QTnb9BQkG4fBYIt9JGvYmxPpd6TBeKp6lsUrtiVQsrJ9sb33Bn9s0wMQO9qVBFbPX3xHRAsBHvXlcsrnJjExjg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script>
        function vPravo () {
            axios.post('/post', {'message':'vPravo'});
            console.log('vPravo');      
        }
        function stop () {
            axios.post(`/stop`);
            console.log('stop');        
        }    
            /*$('#in').keydown(function(e){
                if (e.keyCode == 68) {
                    //$.post('/post', {'message':$(this).val()});
                    $.post('/post', {'message':'painting'});
                    $(this).val('');
                }
            });*/
        </script>

    """


if __name__ == '__main__':
    app.debug = True
    app.run()
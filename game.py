import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)
redis_client = redis.Redis(host='localhost',port=6379, db=0)

string = 'Game started!'
print(redis_client.set(name='score',value=string))

# pubsub() method creates the pubsub object
# but why i named it mobile 🧐
# just kidding 😂 think of it as the waki taki that listens for incomming messages
mobile = r.pubsub()

# use .subscribe() method to subscribe to topic on which you want to listen for messages
mobile.subscribe('army-camp-1')

# .listen() returns a generator over which you can iterate and listen for messages from publisher

for message in mobile.listen():
    score = str(redis_client.get('score'))
    print(score) # <-- you can literally do any thing with this message i am just printing it
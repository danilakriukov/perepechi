import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)
redis_client = redis.Redis(host='localhost',port=6379, db=0)

while True:
	print('Нажмите ф и Энтер, чтоб двигать перса влево')
	print('Нажмите в и Энтер, чтоб двигать перса влево')
	print('Нажмите один пробел и Энтер, чтоб красить')
	move = input()
	if move =='ф':	
		score = redis_client.get('score')
		print(score)
		score = 'vlevo'
		redis_client.set(name='score',value=score)
		r.publish("army-camp-1", score)
	elif move =='в':
		score = redis_client.get('score')
		print(score)
		score = 'vpravo'
		redis_client.set(name='score',value=score)
		r.publish("army-camp-1", score)	
	elif move ==' ':
		score = redis_client.get('score')
		print(score)
		score = 'krasit'
		redis_client.set(name='score',value=score)
		r.publish("army-camp-1", score)		
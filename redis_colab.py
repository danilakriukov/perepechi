import redis

redis_client = redis.Redis(host='localhost',port=6379, db=0)
print(redis_client)
#redis_client.set(name='score',value=10)

#print(redis_client.set(name='score',value=0))
score = int(redis_client.get('score'))
print(score)
print('Нажмите Энтер, чтоб обновить счёт')
input()
score = score + 1
redis_client.set(name='score',value=score)
score = int(redis_client.get('score'))
print(score)
redis_client.close()
input()
# Нужно запустить сначала клиент, потом сервер или на оборот , и 
# и в папке с Редисом на компьютере нужно запустить терминал 
# redis cli , LRANGE queue 0 -1 и появится очередь ... 



from tkinter import DISABLED
import redis
import random


with redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(0, 10))
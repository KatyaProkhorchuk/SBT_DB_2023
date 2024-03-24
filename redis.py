import redis
import time
from datetime import datetime
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
from redis.cluster import RedisCluster as RC
import json
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def to_float(key):
    float_res = 0.0
    key = key.upper()
    for w in key:
        float_res += LETTERS.find(w)
    return float_res


with open('temp.json', 'r') as f:
    data = json.load(f)
data = data['dt']

# Строки - самый простой тип в Redis. Строки Redis хранят последовательности байтов,
# включая текст, сериализованные объекты и двоичные массивы. Они часто используются для кэширования
stringRedis = redis.Redis(host='localhost', port=6379, db=0)
start_time = time.time()
string_set_times = []
string_get_times = []
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        string_set_times.append(time.time() - start_time)
    stringRedis.set(f'airports_json_{key}', json.dumps(value))
end_time = time.time()
print("Total time set string:", end_time - start_time, "seconds")
start_time = time.time()
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        string_get_times.append(time.time() - start_time)

    stringRedis.get(f'airports_json_{key}')
end_time = time.time()
print("Total time get string:", end_time - start_time, "seconds")
print('\n')
file_path1 = 'string_set_times.txt'
file_path2 = 'string_get_times.txt'

# Запись массивов в текстовые файлы что б потом графики сделать
with open(file_path1, 'w') as file1:
    for item in string_get_times:
        file1.write(str(item) + '\n')

with open(file_path2, 'w') as file2:
    for item in string_get_times:
        file2.write(str(item) + '\n')
# Сохранение в виде хэша. Хэш занимает мало места и за счет этого можно сохранить большее кол-во объектов
hash = redis.Redis(host='localhost', port=6379, db=0)
hash_set_times = []
hash_get_times = []
start_time = time.time()
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        hash_set_times.append(time.time() - start_time)
    hash.hset(f'airports_hash', key, json.dumps(value))
end_time = time.time()
print("Total time set hash:", end_time - start_time, "seconds")
start_time = time.time()
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        hash_get_times.append(time.time() - start_time)
    hash.hget(f'airports_hash', key)
end_time = time.time()
print("Total time get hash:", end_time - start_time, "seconds")
print('\n')
file_path1 = 'hash_set_times.txt'
file_path2 = 'hash_get_times.txt'

# Запись массивов в текстовые файлы что б потом графики сделать
with open(file_path1, 'w') as file1:
    for item in hash_set_times:
        file1.write(str(item) + '\n')

with open(file_path2, 'w') as file2:
    for item in hash_get_times:
        file2.write(str(item) + '\n')
# Сохрание в виде сортированного множества.

sortedSet = redis.StrictRedis(host='localhost', port=6379, db=0)
start_time = time.time()
sorted_set_set_times = []
sorted_set_get_times = []
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        sorted_set_set_times.append(time.time() - start_time)
    sortedSet.zadd(f'airports_zset', {json.dumps(value): key})
end_time = time.time()
print("Total time set sorted set:", end_time - start_time, "seconds")
start_time = time.time()
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        sorted_set_get_times.append(time.time() - start_time)
    sortedSet.zrange(f'airports_zset', i, i + 1, withscores=True)
end_time = time.time()
print("Total time get sorted set:", end_time - start_time, "seconds")
print('\n')
file_path1 = 'sorted_set_set_times.txt'
file_path2 = 'sorted_set_get_times.txt'

# Запись массивов в текстовые файлы что б потом графики сделать
with open(file_path1, 'w') as file1:
    for item in sorted_set_set_times:
        file1.write(str(item) + '\n')

with open(file_path2, 'w') as file2:
    for item in sorted_set_get_times:
        file2.write(str(item) + '\n')
# Сохранение в виде списка. Списки Redis - это просто списки строк, отсортированные в порядке вставки. Можно добавлять элементы в список Redis, вставляя новые элементы в голову (слева) или в хвост (справа) списка.
# Команда LPUSH вставляет новый элемент в голову, а RPUSH вставляет новый элемент в хвост. Новый список создается, когда одна из этих операций выполняется против пустого ключа. Аналогично ключ удаляется из пространства ключей, если операция со списком опустошает список.
# Максимальная длина списка составляет 2^32 - 1 элемента
# Так же особенностями списков в редис является поддержка постоянного времени вставки и удаления элементов около головы и хвоста(даже при наличии супер огромного числа элементов)
ListRedis = redis.StrictRedis(host='localhost', port=6379, db=0)
start_time = time.time()
list_set_times = []
list_get_times = []
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        list_set_times.append(time.time() - start_time)
    ListRedis.lpush(f'airports_list', json.dumps(value))
end_time = time.time()
print("Total time set list:", end_time - start_time, "seconds")
start_time = time.time()
for i, (key, value) in enumerate(data.items()):
    if i % 1000 == 0:
        list_get_times.append(time.time() - start_time)
    ListRedis.lrange(f'airports_list', i, i + 1)
end_time = time.time()
print("Total time get list:", end_time - start_time, "seconds")
file_path1 = 'list_set_times.txt'
file_path2 = 'list_get_times.txt'

# Запись массивов в текстовые файлы что б потом графики сделать
with open(file_path1, 'w') as file1:
    for item in list_set_times:
        file1.write(str(item) + '\n')

with open(file_path2, 'w') as file2:
    for item in list_get_times:
        file2.write(str(item) + '\n')


from rediscluster import RedisCluster

startup_nodes = [
    {"host": "172.17.0.2", "port": "6379"},
    {"host": "172.17.0.2", "port": "6380"},
    {"host": "172.17.0.2", "port": "6381"},
]


# Настройки таймаутов (в миллисекундах)
socket_timeout = 3000
socket_connect_timeout = 3000
socket_keepalive = True 

# Создаем кластер Redis с настройками таймаутов
redis_cluster = RedisCluster(
    startup_nodes=startup_nodes,
    decode_responses=True,
    socket_timeout=socket_timeout,
    socket_connect_timeout=socket_connect_timeout,
    socket_keepalive=socket_keepalive
)


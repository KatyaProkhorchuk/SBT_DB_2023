from rediscluster import RedisCluster

startup_nodes = [
    {"host": "172.17.0.2", "port": "7000"},
    {"host": "172.17.0.2", "port": "7001"},
    {"host": "172.17.0.2", "port": "7002"}
]

# Создаем кластер Redis с настройками таймаутов
redis_cluster = RedisCluster(
    startup_nodes=startup_nodes,
    decode_responses=True,
    socket_timeout=1,  # Время ожидания для операций чтения/записи (в секундах)
    socket_connect_timeout=2  # Время ожидания подключения к узлу (в секундах)
)


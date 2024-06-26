## Домашняя работа №2. Redis

### Цель: 

В результате выполнения ДЗ вы научитесь разворачивать Redis в кластере, заполнять данными и делать запросы.

Описание/ инструкция выполнения домашнего задания:

⦁	Сохранить большой JSON (~20МБ) в виде разных структур - строка, hset, zset, list;

⦁	Протестировать скорость сохранения и чтения;

⦁	Настроить редис кластер на 3х нодах с отказоустойчивостью, затюнить 
таймауты.

⦁	Предоставить отчет.



1) Для начала я запустила Redis в докере и создала кластер на 3 нодах с указание необходимых таймаутов. Все `config` лежат в папках 7000, 7001, 7002 - названия соответствуют номерам портов на которых они работают. При запуске контейнера запускается скрипт `run-cluster.sh`. Он запускает три ноды, используя конфиги из их директорий, переводит их в режим кластера и засыпает. Конфиги одиннаковые, отличаются только номерами портов.

   Что бы поднять кластер нужно `docker compose up -d`

   После запуска кластера можно посмотреть, как распределены слоты между нодами.

   ![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/6e9f26b6-12de-4587-bfc2-0f82579251db)


2) Потом нашла нужный json `temp.json`
   
3) Далее (Файл с кодом находится в `redis.py`):

   Сохранила данные из json в формате строки

   Строки - это самый базовый вид значений Redis. Строки Redis являются бинарными, это означает, что строка Redis может содержать любой тип данных, например, изображение JPEG или сериализованный объект Ruby. Длина строкового значения может составлять не более 512 мегабайт.

   Получила следующие результаты времени
   

    ![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/57807267-a9dd-4b4f-b0a9-abc6b60e7e85)


  Теперь хэши.

  Хэш занимает мало места и за счет этого можно сохранить большее кол-во объектов


   ![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/3de17aa9-ac6c-4fe1-80fa-189c986edd6c)


  Сортированные наборы Redis - это, как и наборы Redis, неповторяющиеся коллекции строк. Разница в том, что каждый член сортированного набора ассоциируется с оценкой, которая используется для упорядочивания сортированного набора от наименьшей до наибольшей оценки. В то время как члены уникальны, оценки могут повторяться. Доступ к середине сортированного множества также осуществляется очень быстро

  ![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/af54e946-77be-4904-88cc-453e0f365b29)


  Списки Redis - это просто списки строк, отсортированные в порядке вставки. Можно добавлять элементы в список Redis, вставляя новые элементы в голову (слева) или в хвост (справа) списка.

Команда LPUSH вставляет новый элемент в голову, а RPUSH вставляет новый элемент в хвост. Новый список создается, когда одна из этих операций выполняется против пустого ключа. 


   ![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/61df9f77-dfc8-4eb0-a0ad-cb5e3f548789)

   Сравним графики (графики строила в колабе https://colab.research.google.com/drive/1E6mkDPn7l25cQDZy3JW7goCktz0Z7LpZ?usp=sharing )

   ![Без имени-1](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/9c6c2876-54e5-428f-a85e-bd6aa1bd9ff1)


   ![Без имени](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/7ed6a3d5-4431-4599-9a05-f71181fa6bbf)

   Самыми медленными оказались List и Set, при чем заметное замедление наблюдается с увеличением данных(то есть при небольшом кол-ве данных все ведут себя примерно одинаково)

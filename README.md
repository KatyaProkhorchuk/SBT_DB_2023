# SBT_DB_2023

Для начала установила сервер mongodb что бы запустить локально. И конечно же compass и подключилась к локальному серверу mongobd

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/d853fced-cea6-426f-bb8f-44b855785d5e)

Далее я выбрала вот такой датасет https://www.kaggle.com/datasets/shwetabh123/mall-customers?resource=download

Импортировала датасет

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/23ffa3dc-7e68-4a6d-8d0a-b0fc0c997887)

Дальше я попробовала выполнить CRUD 

## C

Для начала я решила добавить нового пользователя

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/f04ea139-638f-4be3-862c-58580457feca)

## R

Далее я решила посмотреть сколько пользователей 30 лет в таблице

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/a6da9864-e6b6-4a07-b23d-529dd28bd28b)

## U

Далее я обновила возраст покупателя(просто что бы проверить действительно ли поле обновится)

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/ea430b76-e793-4d1e-b059-ecf9f49fe551)

## D

Теперь я хотела удалить тех у кого зарплата меньше 10к$, но таких не оказалось)))

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/743b4bf7-36b4-4280-aff0-008a2896b6fd)


Теперь я решила попробовать агрегацию и посмотреть статистику сколько мужчин/женщин, их средняя зарплата и траты

![изображение](https://github.com/KatyaProkhorchuk/SBT_DB_2023/assets/77965300/7dcbc683-a762-4b82-afcf-325ca390d54d)

Потом я решила добавить фильтр и посмотреть аналогичную статистику, но для людей стареше 30 лет, для этого использовала `$match`

![Uploading изображение.png…]()

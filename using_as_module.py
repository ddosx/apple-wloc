# Подключение appleloc к программе
from appleloc import search as appleloc

# Переменная mac
mac = "b4:5d:50:8f:27:c1"

# Начинаем поиск по переменной mac
# и сохранияем результат

# Функция search выдаёт кортеж из 
# результата(нашло ли?, bool) и списка 
# {
#   "mac": mac адресс ТД,
#   "lat";"long" - Координаты,
#   "altitude" - Высота,
#   "accuracy" - Точночть,
#   "lastchannel" - Последний канал на котором была ТД (По сервисам apple)
# }
find,wloc = appleloc(mac)

# Если ТД не найдена
if find != True:
    print("AP not found")
    # Выйти
    exit()

# Вытягиваем координаты
lat = wloc["lat"]
long = wloc["long"]
# Высоту
alt = wloc["altitude"]
# Точночть
acc = wloc["accuracy"]
# Посл. канал
channel = wloc["lastchannel"]


# Выводим
print(f"{lat=} {long=} {alt=} {acc=} {channel=}")
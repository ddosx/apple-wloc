# Простая утилита для проверки ТД по серверам Apple Wloc
## Зависимости:
1. ```python3```
2. ```pip3 install protobuf```
3. ```pip3 install rich```

## Использование
```python3 appleloc.py "mac"```

## Пример

```alias py="python3"```

```➜ py appleloc.py b4:5d:50:8f:27:c1```

```(True, {'mac': 'b4:5d:50:8f:27:c1', 'lat': 59.43193054, 'long': 24.761522290000002, 'altitude': 11, 'accuracy': 42, 'lastchannel': 6})```

## Скриншот

![Скриншот](https://github.com/ddosx/apple-wloc/blob/main/img/screenshot.png "Скриншот")

## Как модуль:

### Более подробно см [using_as_module.py](https://github.com/ddosx/apple-wloc/blob/main/using_as_module.py)

1. Положите файлы appleloc.py и location_pb2.py к вашему .py файлу
2. Подключите appleloc к вашей программе ```from appleloc import search as appleloc```
3. используйте ```appleloc(mac)``` чтобы получить координаты ТД

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import location_pb2
import urllib.request, urllib.error, urllib.parse


def search(mac):

     # Запрос
     d = f'\x00\x01\x00\x05en_US\x00\x13com.apple.locationd\x00\x0c8.4.1.12H321\x00\x00\x00\x01\x00\x00\x00\x15\x12\x13\n\x11{mac}'
     d = bytes(d,encoding="utf-8")

     # Хереды
     h = {'User-Agent': 'locationd/1756.1.15 CFNetwork/711.5.6 Darwin/14.0.0', 'Content-Type': 'application/x-www-form-urlencoded'}

     # URL для запроса
     u = 'https://gs-loc.apple.com/clls/wloc'

     # Отправляем ...
     req = urllib.request.Request(u, d)
     req.add_header("User-Agent", h["User-Agent"])
     req.add_header("Content-type", h["Content-Type"])
     handle = urllib.request.urlopen(req)

     # Записываем ответ в переменную data
     data = handle.read()

     # Обрезаем лишнее
     data =  data[(data.find(b"\x00\x00\x00\x01\x00\x00") + 8):]

     # Из protobuf в Response.wifis
     Response = location_pb2.Response()
     Response.ParseFromString(data)

     # Форматируем результат во что-то нормальное
     Wifi = Response.wifis[0]
     if Wifi.location.latitude != 18446744055709551616 and Wifi.channel != 0:
          mac = Wifi.mac
          channel = Wifi.channel
          lat = int(Wifi.location.latitude) * 1e-08
          lng = int(Wifi.location.longitude) * 1e-08
          accuracy = Wifi.location.accuracy
          altitude = Wifi.location.altitude
          
          res = True,{"mac":mac,"lat":lat,"long":lng,"altitude":altitude,"accuracy":accuracy,"lastchannel":channel}
     else:res = False,{"mac":"mac","lat":"lat","long":"lng","altitude":"altitude","accuracy":"accuracy","lastchannel":"channel"}

     # Возвращаем
     return res


if __name__ == "__main__":
     from rich import print
     from sys import argv
     print(search(argv[1]))
     
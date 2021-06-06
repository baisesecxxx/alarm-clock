import requests
import time
import json
import pyttsx3
import pygame
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
#起床铃声
def py_player():
    pygame.mixer.init()
    pygame.mixer.music.load("/mp3/1.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
py_player()
#获取天气
def get_weather():
    url = "http://www.weather.com.cn/data/cityinfo/101040100.html"
    url_get = requests.get(url,headers=headers)
    url_get.encoding="utf-8"
    weather_dict = url_get.json()
    rt = weather_dict['weatherinfo']
    weather = '宝贝：起床了，别睡了，该上班了，爱你哦，{}的温度是 {} 到 {}，天气 {}'
    weather = weather.format(rt['city'],rt['temp1'], rt['temp2'], rt['weather'])
    if '雨' in weather:
        weather += ',在下雨今天别忘记带雨伞哦！'
    say_hi(weather)
#文字转语音播报
def say_hi(weather):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice','zh')
    engine.say(weather)
    engine.runAndWait()
    engine.stop()
if __name__ == '__main__':
    get_weather()
    count = 0
    while (count<2):
        py_player()
        count = count+1
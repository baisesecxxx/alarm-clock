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
    pygame.mixer.init() #初始化
    pygame.mixer.music.load("/mp3/1.mp3") #载入音频资源
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True: #判断音频资源是否被占用，等待第一首播放完毕
        continue
py_player()
#获取天气
def get_weather():
    url = "http://www.weather.com.cn/data/cityinfo/101040100.html" #获取地方天气
    url_get = requests.get(url,headers=headers)
    url_get.encoding="utf-8"  #编码
    weather_dict = url_get.json() #获取json
    rt = weather_dict['weatherinfo']
    weather = '宝贝：起床了，别睡了，该上班了，爱你哦，{}的温度是 {} 到 {}，天气 {}'
    weather = weather.format(rt['city'],rt['temp1'], rt['temp2'], rt['weather']) #获取地区、温度、天气情况
    if '雨' in weather: 
        weather += ',在下雨今天别忘记带雨伞哦！' #如果获取到雨，提醒带伞
    say_hi(weather)
#文字转语音播报
def say_hi(weather):
    engine = pyttsx3.init() #创建对象
    rate = engine.getProperty('rate') #获取当前语速
    engine.setProperty('rate', 140) #设置一个新的语速
    volume = engine.getProperty('volume')# 获取当前的音量
    engine.setProperty('volume',1.0) #设置音量
    voices = engine.getProperty('voices') #获取音色
    engine.setProperty('voice', voices[1].id) #修改音色角色，0为男，1为女
    engine.setProperty('voice','zh') #播报语言，zhy为粤语
    engine.say(weather)
    engine.runAndWait()
    engine.stop()
if __name__ == '__main__':
    get_weather()
    count = 0
    while (count<2):
        py_player()
        count = count+1 #循环播放两次音乐

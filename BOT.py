import time,datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
import Adafruit_DHT
pin=4
sensor=Adafruit_DHT.DHT11

now=datetime.datetime.now()

def action(msg):
    chat_id=msg['chat']['id']
    strin =msg['text']
    command=str(strin.lower())
    print('Recevied:%s'%command)

    if command=='hi':
        telegram_bot.sendMessage(chat_id, str("Hi I am your bot"))
    elif command=='time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+ str(":")+str(now.minute))
    elif command=='temp':
        humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
        #GPIO.output(11,GPIO.HIGH)
        telegram_bot.sendMessage(chat_id, str('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity)))
    #elif command=='light off':
        #GPIO.output(11,GPIO.LOW)
    #elif command== 'how are you?':
       # telegram_bot.sendMessage(chat_id, str("I am fine.."))
    #elif command== 'Where are you?':
        #telegram_bot.sendMessage(chat_id, str("in universe..")) 
    #else:
        #telegram_bot.sendMessage(chat_id, str("Sorry,I don't understand"))
        
        
telegram_bot=telepot.Bot('812151634:AAFrtW12PCgpqnmctAsUIcqYtrvbYG8wEhI')
print(telegram_bot.getMe())
MessageLoop(telegram_bot,action).run_as_thread()
print('Up and Running.....')

while 1:
    time.sleep(10)




import time,datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

now = datetime.datetime.now()

def action(msg):
     chat_id = msg['chat']['id']
     strin= msg['text']
     command = str(strin.lower())

     print('Received : %s' % command)

     if(command == 'hi'):
         telegram_bot.sendMessage(chat_id,str("Hi! This side Katy the Bot"))

     elif(command == 'time'):
         telegram_bot.sendMessage(chat_id,str(now.hour) + str(":") +str(now.minute))

     elif(command == 'shivani'):
         telegram_bot.sendMessage(chat_id,str('I love python'))

     elif(command == 'ledon'):
         GPIO.output(11,GPIO.HIGH)
         telegram_bot.sendMessage(chat_id,str('Light is On'))
         
     elif(command == 'ledoff'):
         GPIO.output(11,GPIO.LOW)
         telegram_bot.sendMessage(chat_id,str('Light is Off'))  

     else :
         telegram_bot.sendMessage(chat_id,str("Pardon me! Please repeat"))

telegram_bot=telepot.Bot('878473951:AAFQHgiyt7e7qb8u3bjDuH7jz4qGkjy9y2U')
print(telegram_bot.getMe())

MessageLoop(telegram_bot,action).run_as_thread()
print('Program is loading...')

while 1:
    time.sleep(10)

import requests
import os
import time
import subprocess
from subprocess import Popen, DEVNULL
import socket
import sys
import datetime
from datetime import datetime
from subprocess import call

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1322504589:AAEggDtxjh7jKvayd1uYm3d5Zy9WRDXbKd8'
    bot_chatID = '1372613452'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


### running bash command "date" and then print it out -- РАБОТИ !
#p = subprocess.Popen(["date"], shell=True, stdout=subprocess.PIPE)
#stdout = p.communicate()
# print(str(stdout))

######## start ##########
# to try readning the "hosts" from a file (it will be better, because of a easier modification of hosts. Let's try
######## end ############

############
### testing 19.08.2020, I want to add "ping" command to test it and to send the result through the telegram bot... let's do it !
host = "10.19.8.1" 
ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

stdout, error = ping.communicate()
print(str(stdout))

test = telegram_bot_sendtext(str(stdout))


###
host = "10.19.8.5" 
ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

stdout, error = ping.communicate()
print(str(stdout))

test = telegram_bot_sendtext(str(stdout))


###
host = "127.0.0.1" 
ping = subprocess.Popen(
    ["ping", "-c", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

stdout, error = ping.communicate()
print(str(stdout))


### redirect the command output to a file, using "sys.stdout" 
sys.stdout = open('ping-results.txt', 'a+')
n = datetime.now()
with open("ping-results.txt", "a+") as myfile:
    myfile.write("-------\n")
    myfile.write("%s"%n)
    myfile.write("\n")
    myfile.write("-------\n")
print(str(stdout))

### It works!
#############

### send message to the Telegram Bot, the output of "date" will be send, It needs to be "str", It cannot send "tuple"
test = telegram_bot_sendtext(str(stdout))

# send a mail
with open('/home/mitaka/mail-script.sh', 'rb') as file:
    script = file.read()
rc = call('/home/mitaka/mail-script.sh', shell=True)


### If I want to send just a message
#test = telegram_bot_sendtext('test,test,test,... my result is. test,test,test... my result is...')

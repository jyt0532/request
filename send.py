#Usage: nohup python -u send.py&
import requests
from xml.etree import ElementTree
import datetime
import schedule
import time
#usage: > nohup python -u ./poll.py&
def send():
    target_timestamp = '2016042601+pc-pla'
    url = "XXX"
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    target = tree.find('tag') 	

    current_time = datetime.datetime.now().__str__()

if __name__ == "__main__":
    send()
    schedule.every(1).minutes.do(send)
    while 1:
        schedule.run_pending()
        time.sleep(1)

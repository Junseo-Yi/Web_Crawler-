# 글 보내기
import datetime as dt
import time

from Crawler_4_krGov import main_part
from message_bot import *

while True:
    x = dt.datetime.now()

    if (x.hour == 0):
        tmp = main_part()
        for i in reversed(tmp):
            slack.post_thread_message(channel_id, str(i))

    time.sleep(3600)

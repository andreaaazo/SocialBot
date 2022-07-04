from ast import arg
from asyncio import tasks
from multiprocessing import Event
import threading
from threading import Event, Thread
import time
from instabot import InstagramBot
from tiktokbot import TikTokBot


class SocialThread(threading.Thread):
    def __init__(self, social, account_num):
        super(SocialThread, self).__init__()
        self.stop_event = Event()
        self.social = social
        self.account_num = account_num

    def stop(self):
        self.stop_event.set()

    def run(self):
        if self.social == "Instagram":
            while not self.stop_event.is_set():
                bot = InstagramBot(self.account_num)
                bot.login()
                bot.post()
        else:
            while not self.stop_event.is_set():
                tikbot = TikTokBot(self.account_num)
                tikbot.login()
                tikbot.post()

from multiprocessing import Event
import threading
from threading import Event
from instabot import InstagramBot
from tiktokbot import TikTokBot

thread_dict = dict()


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


class ThreadDictionary:
    def __init__(self, account_num, social) -> None:
        self.account_num = account_num
        self.social = social

    def run_thread(self):
        thread_dict[str(self.social) + str(self.account_num)] = SocialThread(
            self.social, self.account_num
        )
        thread_dict[str(self.social) + str(self.account_num)].start()

    def stop_thread(self):
        thread_dict[str(self.social) + str(self.account_num)].stop()
        thread_dict[str(self.social) + str(self.account_num)] = SocialThread(
            self.social, self.account_num
        )

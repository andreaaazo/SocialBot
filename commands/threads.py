from multiprocessing import Event
import threading
from threading import Event
from commands.instabot import InstagramBot
from commands.tiktokbot import TikTokBot
from commands.statusbar import statusbar_dict

thread_dict = dict()


class SocialThread(threading.Thread):
    def __init__(self, social, account_num):
        super(SocialThread, self).__init__()
        self.stop_event = Event()
        self.social = social
        self.account_num = account_num
        self.status = statusbar_dict[str(self.social) + str(self.account_num)]

    def stop(self):
        self.status.change_text("Finishing task...")
        self.stop_event.set()

    def run(self):
        if self.social == "Instagram":
            while not self.stop_event.is_set():
                instabot = InstagramBot(self.account_num)
                if not self.stop_event.is_set():
                    instabot.login()
                else:
                    pass
                if not self.stop_event.is_set():
                    instabot.post()
                else:
                    pass
            instabot.quit()
        else:
            while not self.stop_event.is_set():
                tikbot = TikTokBot(self.account_num)
                if not self.stop_event.is_set():
                    tikbot.login()
                else:
                    pass
                if not self.stop_event.is_set():
                    tikbot.post()
                else:
                    pass
            tikbot.quit()


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

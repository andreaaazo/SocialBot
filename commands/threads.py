from multiprocessing import Event
import threading
from threading import Event
from commands.instabot import InstagramBot
from commands.tiktokbot import TikTokBot
from commands.statusbar import statusbar_dict
import pickle
from time import sleep

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
        if (
            pickle.load(open("auto_post_settings.pkl", "rb"))[
                str(self.social) + str(self.account_num)
            ]
            == 1
        ):  # Check if auto post is ON
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
                    if not self.stop_event.is_set():
                        self.botrest = pickle.load(
                            open("auto_post_settings.pkl", "rb")
                        )["botsleeping" + str(self.social) + str(self.account_num)]
                        statusbar_dict["Instagram" + str(self.account_num)].change_text(
                            "I'm sleeping for " + str(self.botrest) + " Hours"
                        )
                        sleep(int(self.botrest * 3600))
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
                    if not self.stop_event.is_set():
                        self.botrest = pickle.load(
                            open("auto_post_settings.pkl", "rb")
                        )["botsleeping" + str(self.social) + str(self.account_num)]
                        statusbar_dict["TikTok" + str(self.account_num)].change_text(
                            "I'm sleeping for " + str(self.botrest) + " Hours"
                        )
                        sleep(int(self.botrest * 3600))
                    else:
                        pass
                tikbot.quit()
        else:
            if self.social == "Instagram":
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

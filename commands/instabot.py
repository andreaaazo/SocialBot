from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    InvalidSessionIdException,
    NoSuchWindowException,
    InvalidArgumentException,
)

from urllib3.exceptions import MaxRetryError

from time import sleep

import chromedriver_autoinstaller

from commands.database import Database

from commands.statusbar import statusbar_dict


class InstagramBot:
    def __init__(self, account_num) -> None:
        self.status = statusbar_dict["Instagram" + str(account_num)]

        self.database = Database()
        self.email = str(self.database.insta_bot_informations(account_num)[0])
        self.password = str(self.database.insta_bot_informations(account_num)[1])
        self.description = (
            str(self.database.insta_bot_informations(account_num)[2])
            + "\n"
            + str(self.database.insta_bot_informations(account_num)[3])
        )
        self.path = str(self.database.insta_bot_informations(account_num)[4])

        chromedriver_autoinstaller.install()  # Install driver

        # Tweaks
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--profile-directory=Default")
        self.options.add_argument("--incognito")
        # self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

        # Disable cache
        self.driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled": True})

    def login(self):
        try:
            # Instagram login page
            self.driver.get("https://www.instagram.com/")

            self.status.change_text("Loading instagram login page...")
            self.status.change_text("Page sucessfully loaded")
            self.status.change_text("Getting rid of pop up")

            # Check cookie pop-up
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "aOOlW.HoLwm"))
                )
                self.driver.find_element(By.CLASS_NAME, "aOOlW.HoLwm").click()
                self.status.change_text("Pop up eliminated :)")
            except TimeoutException:
                return self.status.change_text("No pop up :)")

            self.status.change_text("Inserting Instagram credentials")

            # Wait until page loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.XPATH, '//input[@name="username"]')
                    )
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("Failed to load instagram login page")

            # Instagram login
            try:
                self.driver.find_element(
                    By.XPATH, '//input[@name="username"]'
                ).send_keys(self.email)
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to insert instagram login email")

            try:
                self.driver.find_element(
                    By.XPATH, '//input[@name="password"]'
                ).send_keys(self.password)
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to insert instagram password")

            try:
                self.driver.find_element(
                    By.XPATH, '//input[@name="password"]'
                ).send_keys(Keys.ENTER)
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to send Instragram login")

            self.status.change_text("Instagram credentials sucessfully sent")

            # Turning off notifications
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "_a9--._a9_1"))
                )
                self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
            except TimeoutException:
                self.status.change_text("Can't turn off notifications")
                self.driver.quit()

            self.status.change_text("Success login")

        except MaxRetryError:
            return self.status.change_text("Session aborted")

        except InvalidSessionIdException:
            return self.status.change_text("Session aborted")

        except NoSuchWindowException:
            return self.status.change_text("Session aborted")

    def post(self):
        try:
            self.driver.get("https://www.instagram.com/")

            self.status.change_text("Posting...")

            # Turning off notifications
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "_abl-._abm2"))
                )
                self.driver.find_element(By.CLASS_NAME, "_abl-._abm2").click()
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("Can't turn off notifications")

            # Posting video
            try:
                drag_drop = self.driver.find_elements(
                    By.XPATH, '//input[@class="_ac69"]'
                )
                drag_drop[2].send_keys(self.path)
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to drag image or video")
            except InvalidArgumentException:
                return self.status.change_text("Invalid image or video path")

            self.status.change_text("Video successfully uploaded")

            # Wait until page is loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "_ac7b._ac7d"))
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("Unable to post")

            self.status.change_text("Sleeping for 100 seconds to let the video upload")

            sleep(10)

            # Post button
            for _ in range(2):
                try:
                    self.driver.find_element(By.CLASS_NAME, "_ac7b._ac7d").find_element(
                        By.CLASS_NAME, "_acan._acao._acas"
                    ).click()
                    sleep(3)
                except IndexError:
                    self.driver.quit()
                    return self.status.change_text("Unable to click the post button")

            self.status.change_text("Posting video...")

            # Add caption
            try:
                textarea_caption = self.driver.find_element(
                    By.CLASS_NAME,
                    "gs1a9yip.rq0escxv.j83agx80.cbu4d94t.buofh1pr.taijpn5t",
                ).find_elements(By.XPATH, "//textarea")
                self.status.change_text(len(textarea_caption))
                textarea_caption[0].send_keys(self.description)
            except IndexError:
                self.driver.quit()
                return self.status.change_text("Unable to write the caption")

            self.status.change_text("Caption added")

            # Disable likes
            try:
                disableLikes = self.driver.find_element(
                    By.CLASS_NAME,
                    "gs1a9yip.rq0escxv.j83agx80.cbu4d94t.buofh1pr.taijpn5t",
                ).find_elements(By.CLASS_NAME, "_abm9")
                disableLikes[1].click()
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                likesCheckbox = self.driver.find_element(
                    By.CLASS_NAME,
                    "gs1a9yip.rq0escxv.j83agx80.cbu4d94t.buofh1pr.taijpn5t",
                ).find_elements(By.XPATH, '//label[@class="_ac5-"]')
                likesCheckbox[0].click()
            except IndexError:
                self.driver.quit()
                return self.status.change_text("Unable to disable likes")

            self.status.change_text("Likes disabled")

            # Post button
            try:
                self.driver.find_element(By.CLASS_NAME, "_ac7b._ac7d").find_element(
                    By.CLASS_NAME, "_acan._acao._acas"
                ).click()
            except IndexError:
                self.driver.quit()
                return self.status.change_text("Unable to click the post button")

            # Wait until post is posted
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.CLASS_NAME, "_aacl._aacr._aact._aacx._aad6._aadb")
                    )
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text(
                    "Unable to post the video or the video upload took too long"
                )

            # Return to main page
            self.driver.get("https://www.instagram.com/")

        except MaxRetryError:
            return self.status.change_text("Session aborted")

        except InvalidSessionIdException:
            return self.status.change_text("Session aborted")

        except NoSuchWindowException:
            return self.status.change_text("Session aborted")

    def quit(self):
        try:
            self.driver.quit()
        except MaxRetryError:
            return self.status.change_text("Session closed")

        except InvalidSessionIdException:
            return self.status.change_text("Session closed")

        except NoSuchWindowException:
            return self.status.change_text("Session closed")

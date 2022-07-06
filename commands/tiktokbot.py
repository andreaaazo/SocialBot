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
)

from urllib3.exceptions import MaxRetryError

from time import sleep

from commands.database import Database

from commands.statusbar import statusbar_dict

import chromedriver_autoinstaller


class TikTokBot:
    def __init__(self, account_num) -> None:
        self.status = statusbar_dict["TikTok" + str(account_num)]
        self.database = Database()
        self.email = str(self.database.tiktok_bot_informations(account_num)[0])
        self.password = str(self.database.tiktok_bot_informations(account_num)[1])
        self.description = (
            str(self.database.tiktok_bot_informations(account_num)[2])
            + "\n"
            + str(self.database.tiktok_bot_informations(account_num)[3])
        )
        self.path = str(self.database.tiktok_bot_informations(account_num)[4])

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
            # Facebook login page
            self.status.change_text("Loading facebook login page...")
            self.driver.get("https://shorturl.at/cyzCN")

            # Wait until page loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.ID, "booklet"))
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("Failed to load facebook login page")

            self.status.change_text("Page sucessfully loaded")
            self.status.change_text("Getting rid of pop up")

            # Check cookie pop-up
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.CLASS_NAME, "_42ft._4jy0._9xo7._4jy3._4jy1.selected._51sy")
                    )
                )
                self.driver.find_element(
                    By.CLASS_NAME, "_42ft._4jy0._9xo7._4jy3._4jy1.selected._51sy"
                ).click()
                self.status.change_text("Pop up eliminated :)")
            except TimeoutException:
                return self.status.change_text("No pop up :)")

            self.status.change_text("Inserting facebook credentials")

            # Wait until page loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located((By.XPATH, '//input[@id="email"]'))
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("Failed to load facebook login page")

            # Facebook login
            try:
                self.driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(
                    self.email
                )
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to insert facebook login email")

            try:
                self.driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(
                    self.password
                )
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to insert facebook password")

            try:
                self.driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(
                    Keys.ENTER
                )
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to send Facebook login")

            self.status.change_text("Facebook credentials sucessfully sent")

            # Wait until page loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.CLASS_NAME, "channel-item-wrapper-2gBWB")
                    )
                )
            except TimeoutException:
                try:
                    self.driver.refresh()
                    WebDriverWait(self.driver, 30).until(
                        ec.presence_of_element_located(
                            (By.CLASS_NAME, "channel-item-wrapper-2gBWB")
                        )
                    )
                except TimeoutException:
                    try:
                        WebDriverWait(self.driver, 60).until(
                            ec.presence_of_element_located(
                                (
                                    By.CLASS_NAME,
                                    "tiktok-xbg2z9-DivBoxContainer.e1cgu1qo0",
                                )
                            )
                        )
                    except TimeoutException:
                        self.driver.quit()
                        return self.status.change_text(
                            "Failed to connect to TikTok page"
                        )

            # TikTok login button
            try:
                divArray = self.driver.find_elements(
                    By.CLASS_NAME, "channel-item-wrapper-2gBWB"
                )
                if not divArray:
                    divArray = self.driver.find_elements(
                        By.CLASS_NAME, "tiktok-xbg2z9-DivBoxContainer.e1cgu1qo0"
                    )
                    divArray[2].click()
                else:
                    divArray[2].click()
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to click TikTok login button")
            except IndexError:
                self.driver.quit()
                return self.status.change_text("Failed to click TikTok login button")

            # Wait until tiktok home loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.CLASS_NAME, "tiktok-r0hg2a-DivSideNavContainer.e1irlpdw1")
                    )
                )
            except TimeoutException:
                return self.status.change_text("Failed to connect to TikTok")

            self.status.change_text("Success login")
        except MaxRetryError:
            return self.status.change_text("Session aborted")

        except InvalidSessionIdException:
            return self.status.change_text("Session aborted")

        except NoSuchWindowException:
            return self.status.change_text("Session aborted")

    def post(self):
        try:
            self.status.change_text("Posting...")
            self.driver.get("https://www.tiktok.com/upload")
            self.status.change_text("Waiting page to load...")

            # Switching to iframe
            self.driver.switch_to.frame(
                self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe')
            )

            # Wait until TikTok upload page loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.CLASS_NAME, "jsx-1717967343.text-container")
                    )
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("TikTok upload page failed connection")

            self.status.change_text("Page successfully loaded")
            self.status.change_text("Uploading video...")

            # Uploading the video
            try:
                self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(
                    self.path
                )
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Failed to upload the video")

            self.status.change_text("Video successfully uploaded")
            self.status.change_text("Writing caption...")

            # Wait until page is fully loaded
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div',
                        )
                    )
                )
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text("TikTok Uploading page not fully loaded")

            # Writing caption
            try:
                self.driver.find_element(
                    By.XPATH,
                    '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div',
                ).clear()
                self.driver.find_element(
                    By.XPATH,
                    '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div',
                ).send_keys(" " + self.description)
            except NoSuchElementException:
                self.driver.quit()
                return self.status.change_text("Unable to find the caption input")

            self.status.change_text("Caption successfully wrote")
            self.status.change_text("Waiting 100 seconds to let the video upload")

            sleep(100)

            self.status.change_text("Let's smash this post!")

            # Scoll down to avoid cookie pop-up
            self.driver.switch_to.default_content()
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            self.driver.switch_to.frame(
                self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe')
            )

            self.status.change_text("Posting video...")

            # Clicking upload button
            try:
                WebDriverWait(self.driver, 60).until(
                    ec.presence_of_element_located(
                        (By.XPATH, '//button[@class="css-n99h88"]')
                    )
                )
                self.driver.find_element(
                    By.XPATH, '//button[@class="css-n99h88"]'
                ).click()
            except TimeoutException:
                self.driver.quit()
                return self.status.change_text(
                    "Unable to find the post button or the video upload took too long"
                )

            self.status.change_text("Video successfully posted")

            # Get to TikTok Home
            sleep(10)
            self.driver.get("https://www.tiktok.com")
            self.driver.quit()

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

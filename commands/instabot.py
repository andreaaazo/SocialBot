from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSessionIdException, NoSuchWindowException, InvalidArgumentException

from urllib3.exceptions import MaxRetryError

from time import sleep

import chromedriver_autoinstaller


class InstagramBot:
	def boot(self):
		chromedriver_autoinstaller.install() # Install driver

		# Tweaks
		self.options = Options()
		self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.options.add_experimental_option('useAutomationExtension', False)
		self.options.add_argument('--disable-blink-features=AutomationControlled')
		self.options.add_argument("--profile-directory=Default")
		self.options.add_argument("--incognito")
		#self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(options=self.options)

		# Disable cache
		self.driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":True})
	

	def login(self):
		try:
			# Instagram login page
			print("Loading instagram login page...")
			
			self.driver.get("https://www.instagram.com/")
			
			print("Page sucessfully loaded")
			print("Getting rid of pop up")
			
			# Check cookie pop-up
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
					(By.CLASS_NAME, 'aOOlW.HoLwm')))
				self.driver.find_element(By.CLASS_NAME, 'aOOlW.HoLwm').click()
				print("Pop up eliminated :)")
			except TimeoutException:
				return print("No pop up :)")

			print("Inserting Instagram credentials")

			# Wait until page loaded
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
					(By.XPATH, '//input[@name="username"]')))
			except TimeoutException:
				self.driver.quit()
				return print('Failed to load instagram login page')

			# Instagram login
			try:
				self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('jdm.crew@outlook.com')
			except NoSuchElementException:
				self.driver.quit()
				return print('Failed to insert instagram login email')
			
			try:
				self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Andrea23')
			except NoSuchElementException:
				self.driver.quit()
				return print('Failed to insert instagram password')

			try:
				self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(Keys.ENTER)		
			except NoSuchElementException:
				self.driver.quit()
				return print('Failed to send Instragram login')
			
			print("Instagram credentials sucessfully sent")
			
			# Turning off notifications
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(By.CLASS_NAME, "_a9--._a9_1")))
				self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
			except TimeoutException:
				print("Can't turn off notifications")
				self.driver.quit()
			

			print("Success login")

		except MaxRetryError:
			return print("Session aborted")

		except InvalidSessionIdException:
			return print("Session aborted")

		except NoSuchWindowException:
			return print("Session aborted")


	def post(self):
		try:
			print("Posting...")
			
			self.driver.get("https://www.instagram.com/")

			# Turning off notifications
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(By.CLASS_NAME, "_abl-._abm2")))
				self.driver.find_element(By.CLASS_NAME, "_abl-._abm2").click()
			except TimeoutException:
				self.driver.quit()
				return print("Can't turn off notifications")
			
			# Posting video
			try:
				drag_drop = self.driver.find_elements(By.XPATH, '//input[@class="_ac69"]')
				drag_drop[1].send_keys('/Users/andreazorzi/Desktop/SocialBot 2.2/test.mp4')
			except NoSuchElementException:
				self.driver.quit()
				return print('Failed to drag image or video')
			except InvalidArgumentException:
				return print("Invalid image or video path")

			print("Video successfully uploaded")

			# Wait until page is loaded
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(By.CLASS_NAME, "_acan._acao._acas")))
			except TimeoutException:
				self.driver.quit()
				return print("Unable to post")

			# Active element
			self.driver.switch_to_active_element()


			# Post button
			for _ in range(2):
				try:
					post_button = self.driver.find_elements(By.XPATH, '//button[@class="_acan _acao _acas"]')
					post_button[2].click()
					sleep(3)
				except IndexError:
					self.driver.quit()
					return print("Unable to click the post button")
			
			print("Posting video...")
		
			# Add caption
			try:
				textarea_caption = self.driver.find_elements(By.XPATH, '//textarea')
				textarea_caption[0].send_keys('caption')
			except IndexError:
				self.driver.quit()
				return print("Unable to write the caption")
		
			print("Caption added")

			# Disable likes
			try:
				disableLikes = self.driver.find_elements(By.CLASS_NAME, '_abm9')
				disableLikes[1].click()
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				likesCheckbox = self.driver.find_elements(By.XPATH, '//label[@class="_ac5-"]')
				likesCheckbox[0].click()
			except IndexError:
				self.driver.quit()
				return print("Unable to disable likes")
			
			print("Likes disabled")

			# Post button
			try:
				post_button = self.driver.find_elements(By.CLASS_NAME, '_acan._acao._acas')
				post_button[0].click()
			except IndexError:
				self.driver.quit()
				return print("Unable to click the post button")
			
			# Wait until post is posted
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, '_aacl._aacr._aact._aacx._aad6._aadb')))
			except TimeoutException:
				self.driver.quit()
				return print("Unable to post the video or the video upload took too long")

			# Return to main page
			self.driver.get("https://www.instagram.com/")

		except MaxRetryError:
			return print("Session aborted")

		except InvalidSessionIdException:
			return print("Session aborted")

		except NoSuchWindowException:
			return print("Session aborted")

if __name__ == '__main__':
	bot = InstagramBot()
	bot.boot()
	bot.login()
	bot.post()
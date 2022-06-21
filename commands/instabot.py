from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSessionIdException, NoSuchWindowException

from urllib3.exceptions import MaxRetryError

from time import sleep

import chromedriver_autoinstaller


class TikTokBot:
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
	

	def tiktoklogin(self):

		sleep(4)

		try:
			# Facebook login page
			print("Loading instagram login page...")
			self.driver.get("https://www.instagram.com/")
			
			# Wait until page loaded
			""" try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
					(By.ID, 'booklet')))
			except TimeoutException:
				self.driver.quit()
				return print('Failed to load facebook login page') """

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
			
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(By.CLASS_NAME, "_a9--._a9_1")))
				self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
			except TimeoutException:
				print("Can't turn off notifications")
				self.driver.quit()
			
			# Wait until page loaded
			""" try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'channel-item-wrapper-2gBWB')))
			except TimeoutException:
				try:
					self.driver.refresh()
					WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(
						(By.CLASS_NAME, 'channel-item-wrapper-2gBWB')))
				except TimeoutException:
					try:
						WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'tiktok-xbg2z9-DivBoxContainer.e1cgu1qo0')))
					except TimeoutException:
						self.driver.quit()
						return print("Failed to connect to TikTok page") """
			
			# Instagram login button
			""" try:
				divArray = self.driver.find_elements(By.CLASS_NAME, 'channel-item-wrapper-2gBWB')
				if not divArray:
					divArray = self.driver.find_elements(By.CLASS_NAME, 'tiktok-xbg2z9-DivBoxContainer.e1cgu1qo0')
					divArray[2].click()
				else:
					divArray[2].click()
			except NoSuchElementException:
				self.driver.quit()
				return print("Failed to click TikTok login button")
			except IndexError:
				self.driver.quit()
				return print("Failed to click TikTok login button")
					
			# Wait until tiktok home loaded
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'tiktok-r0hg2a-DivSideNavContainer.e1irlpdw1')))
			except TimeoutException:
				return print("Failed to connect to Instagram") """

			print("Success login")
		except MaxRetryError:
			return print("Session aborted")

		except InvalidSessionIdException:
			return print("Session aborted")

		except NoSuchWindowException:
			return print("Session aborted")


	def tiktokpost(self):
		try:
			print("Posting...")

			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(By.CLASS_NAME, "_abl-._abm2")))
				self.driver.find_element(By.CLASS_NAME, "_abl-._abm2").click()
			except TimeoutException:
				print("Can't turn off notifications")
				self.driver.quit()
			
			try:
				drag_drop = self.driver.find_elements(By.XPATH, '//input[@class="_ac69"]')
				drag_drop[1].send_keys('/home/losilof39/Documents/repos/SocialBot/test.mp4')
			except NoSuchElementException:
				self.driver.quit()
				return print('Failed to drag image or video')
			

			#self.driver.get("https://www.tiktok.com/upload")
			#print("Waiting page to load...")
			
			# Switching to iframe
			""" self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe'))

			# Wait until TikTok upload page loaded
			try: 
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, "jsx-1717967343.text-container")))
			except TimeoutException:
				self.driver.quit()
				return print("TikTok upload page failed connection")
			
			print("Page successfully loaded")
			print("Uploading video...")

			# Uploading the video
			try:
				self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys('/home/losilof39/Documents/repos/SocialBot/test.mp4')
			except NoSuchElementException:
				self.driver.quit()
				return print("Failed to upload the video")
			
			print("Video successfully uploaded")
			print("Writing caption...")

			# Wait until page is fully loaded
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div')))
			except TimeoutException:
				self.driver.quit()
				return print("TikTok Uploading page not fully loaded")

			# Writing caption
			try:
				self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div').clear()
				self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div').send_keys(' '+ 'caption')
			except NoSuchElementException:
				self.driver.quit()
				return print("Unable to find the caption input")
			
			print("Caption successfully wrote")
			print("Waiting 100 seconds to let the video upload")
			
			sleep(100)
			
			print("Let's smash this post!")
			
			# Scoll down to avoid cookie pop-up
			self.driver.switch_to.default_content()
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe'))

			print("Posting video...")

			# Clicking upload button
			try:
				WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.XPATH, '//button[@class="css-n99h88"]')))
				self.driver.find_element(By.XPATH, '//button[@class="css-n99h88"]').click()
			except TimeoutException:
				self.driver.quit()
				return print("Unable to find the post button or the video upload took too long")
			
			print("Video successfully posted")

			# Get to TikTok Home
			sleep(10)
			self.driver.get("https://www.tiktok.com")
			self.driver.quit() """

		except MaxRetryError:
			return print("Session aborted")

		except InvalidSessionIdException:
			return print("Session aborted")

		except NoSuchWindowException:
			return print("Session aborted")

if __name__ == '__main__':
	bot = TikTokBot()
	bot.boot()
	bot.tiktoklogin()
	bot.tiktokpost()
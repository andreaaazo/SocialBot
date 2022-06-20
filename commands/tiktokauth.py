from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

class TikTokBot:
	def __init__(self):
		chromedriver_autoinstaller.install()
		self.options = Options()
		self.driver = webdriver.Chrome(options=self.options)

		# tweaks

		self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.options.add_experimental_option('useAutomationExtension', False)
		self.options.add_argument('--disable-blink-features=AutomationControlled')
		self.options.add_argument("--profile-directory=Default")
		self.options.add_argument("--incognito")

	# Shortcuts
	def loadingPage(self, elementName, elementPath, text):
		try:
			WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(elementName, elementPath)))  # Check webpage charged
		except TimeoutException:
			print(text)
			self.driver.quit()

	def click(self, elementName, elementPath, text):
		try:
			self.driver.find_element(elementName, elementPath).click()
		except NoSuchElementException:
			print(text)
			self.driver.quit()

	def type(self, elementName, elementPath, text, errortext):
		try:
			self.driver.find_element(elementName, elementPath).send_keys(text)
		except NoSuchElementException:
			print(errortext)
			self.driver.quit()

	def check(self, elementName, elementPath, text):
		try:
			WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(
				(elementName, elementPath)))
			self.driver.find_element(elementName, elementPath).click()
		except TimeoutException:
			print(text)
			self.driver.quit()

	def TikTokAuth(self):
		print("Loading facebook login page...")
		self.driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fclient_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_cfiw12km%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D38eae226-6069-4ac9-af15-f58386034b25%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_cfiw12km%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=popup&locale=it_IT&pl_dbl=0")
		self.loadingPage(By.ID, 'booklet', "failed to load facebook login page")
		print("Page sucessfully loaded")
		print("Getting rid of pop up")
		self.check(By.CLASS_NAME, '_42ft._4jy0._9xo7._4jy3._4jy1.selected._51sy', "can't get rid of cookie pop up")  # cookie pop up
		print("Pop up eliminated :)")
		print("Inserting facebook credentials")
		self.loadingPage(By.XPATH, '//input[@id="email"]', "failed to load facebook login page")
		self.type(By.XPATH, '//input[@id="email"]', "jdm.crew@outlook.com", "failed to insert facebook login email")
		self.type(By.XPATH, '//input[@id="pass"]', "Andrea23", "failed to insert facebook login password")
		self.type(By.XPATH, '//input[@id="pass"]', Keys.ENTER, "failed to send facebook login credentials")
		print("Facebook credentials sucessfully sent")
		self.check(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]', "failed to connect")  # Use /html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3] or /html/body/div[2]/div/div[2]/div/div/div[3]
		self.loadingPage(By.CLASS_NAME, "tiktok-1id9666-DivMainContainer.ec6jhlz0", "TikTok page connection failed")
		print("Success login")

	def TikTokPost(self):
		print("Posting...")
		self.driver.get("https://www.tiktok.com/upload?lang=it-IT")
		print("Waiting page to load...")
		self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe"))  # switching to iframe
		self.loadingPage(By.CLASS_NAME, 'jsx-1717967343.text-container', "failed to connect to tiktok uploading page")
		print("Page successfully loaded")
		print("Uploading video...")
		self.type(By.XPATH, '//input[@type="file"]', '/Users/andreazorzi/Desktop/SocialBot 2.1/test.mp4', "failed to upload the video")
		print("Video successfully uploaded")
		print("Writing caption...")
		self.loadingPage(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div', "unable to write the caption")
		try:
			self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div').clear()
			self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div').send_keys('hello there!')
		except NoSuchElementException:
			print("Unable to find the caption input")
			self.driver.quit()
		print("Caption successfully wrote")
		print("Waiting 100 seconds to let the video upload")
		sleep(100)
		print("Let's smash this post!")
		print("Posting video...")
		self.click(By.XPATH, '//button[@class="css-n99h88"]', "unable to find the post button or video upload took  too long")
		print("Video successfully posted")


if __name__ == '__main__':
	bot = TikTokBot()
	bot.TikTokAuth()
	bot.TikTokPost()

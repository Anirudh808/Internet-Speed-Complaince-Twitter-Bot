from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "anirudhmounasamy.tech@gmail.com"
TWITTER_PASSWORD = "Ani@Twitter$2004*"
TWITTER_USERNAME = "m1532161"
x_url = "https://x.com"
speed_test_url = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 180)

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[4]/div[1]/div[3]/div/div/div/div[3]/span')))
        speed_test_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[2]/a')
        speed_test_button.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')))
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = float(upload_speed)
        self.down = float(download_speed)
        print(f"Down: {download_speed}\nupload: {upload_speed}")

    def tweet_at_provider(self):
        self.driver.get(x_url)

        signin_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')
        if not signin_button:
            signin_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/a')
        signin_button.click()

        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        email_input.send_keys(TWITTER_EMAIL, Keys.ENTER)

        try:
            wait = WebDriverWait(self.driver, 5)
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            username_input.send_keys(TWITTER_USERNAME, Keys.ENTER)
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
            password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            post_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')))
            post_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

            post_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')))
            post_button.click()

            print("Tweeted")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

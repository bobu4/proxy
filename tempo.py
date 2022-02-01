from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'MY_KEY')
solver = TwoCaptcha(api_key)

ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://coinlist.co/register')
key = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '''//*[@id='new_user']/div/div[6]/h-captcha''')))
try:
    result = solver.hcaptcha(
        sitekey=key.get_attribute("sitekey"),
        url=driver.current_url,
    )

except Exception as e:
    print(e)

else:
    print('result: ' + str(result))
    print(result['code'])
driver.execute_script(f"hcaptcha.getResponse = function(){{return '{result['code']}'}}")
time.sleep(3)

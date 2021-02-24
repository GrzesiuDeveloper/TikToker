from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import system
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options2 = webdriver.ChromeOptions()
options2.add_argument("--no-sandbox")
options2.add_argument("--incognito")
options2.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome("chromedriver", options = options)
driver2 = webdriver.Chrome("chromedriver", options = options2)

def loop():
    sleep(60)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        driver2.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    except:
        driver.refresh()
        driver2.refresh()
        loop()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        driver2.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        driver2.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver2.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver.refresh()
        driver2.refresh()
        loop()
    except:
        driver.refresh()
        driver2.refresh()
        loop()

print("---TikTok Viewbot---")
print("My GitHub: recanman")
print("How this works is that it uses Selenium to click buttons and type in your URL in an external service that gives views. It would be really expensive to keep up a network of bots for viewbotting use. I cannot guarantee that te website will be up though.")
sleep(2)
vidUrl = input("Please input your video url (It should look like this: https://www.tiktok.com/@USERNAME/video/VIDEOID)\n> ")
print("Solve the captcha in the web browser to continue, then you should be good to go! Leave it running overnight or while you work, this does not use a lot of resources.")

driver.get("https://zefoy.com/")
driver2.get("https://zefoy.com/")
loop()

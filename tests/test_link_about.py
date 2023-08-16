from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pages.login_page import Login_page
from pages.main_page import Main_page



def test_link_about():
    s = Service('C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")


    time.sleep(5)




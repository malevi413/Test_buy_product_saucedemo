from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.client_confirmation import Client_confirmation_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=2)
def test_buy_product_1(set_group):
    s = Service('C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print("Start Test1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()
    #
    cc = Client_confirmation_page(driver)
    cc.client_confirmation()

    pp = Payment_page(driver)
    pp.finish_click()

    fp = Finish_page(driver)
    fp.finish()

    driver.quit()


# @pytest.mark.run(order=1)
def test_buy_product_2(set_group):
    s = Service('C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print("Start Test2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    driver.quit()


# @pytest.mark.run(order=3)
def test_buy_product_3():
    s = Service('C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print("Start Test3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    driver.quit()
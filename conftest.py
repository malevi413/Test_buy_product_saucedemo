import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True, scope="class")
def driver():
    # инициализация браузера
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy'] = 'eager'
    s = Service('C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, desired_capabilities=capabilities)

    yield driver
    driver.quit()


@pytest.fixture()
def set_up():
    print('Start test')
    yield
    print('Finish test')


@pytest.fixture(scope='module')
def set_group():
    print('Enter system')
    yield
    print('Exit system')

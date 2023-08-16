from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    # Locators
    button_checkout = "//button[@id='checkout']"

    # Getters
    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Actions
    def click_button_checkout(self):
        self.get_button_checkout().click()
        print('Click checkout button')

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_button_checkout()

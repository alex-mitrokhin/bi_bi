from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы Корзина """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    registration_button = '//a[@class="app-button app-button--yellow"]'


    # Getters
    def get_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))


    # Actions
    def click_registration_button(self):
        self.get_registration_button().click()
        print('Click registration button')


    # Methods
    def product_confirmation(self):
        """ Подтверждение товара """
        self.get_current_url()
        self.click_registration_button()


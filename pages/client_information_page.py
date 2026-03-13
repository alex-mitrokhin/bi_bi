from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ClientInformationPage(Base):
    """ Класс содержащий локаторы и методы для страницы Информации о клиенте """


    # Locators

    first_name = '(//input[@class="input-mask"])[1]'
    phone = '(//input[@class="input-mask"])[3]'
    payment_method = '(//span[@class="payment__icon"])[2]'
    arrange_button = '//button[@class="app-button app-button--yellow checkout-sidebar__submit mobile-shift"]'
    main_word = '//h3[@class="title _popup-title_10d5o_9"]'


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method)))

    def get_arrange_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrange_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('Input phone')

    def click_payment_method(self):
        self.get_payment_method().click()
        print('Click payment_method')

    def click_arrange_button(self):
        self.get_arrange_button().click()
        print('Click Arrange_button')


    # Methods

    def input_information(self):
        """ Ввод информации о клиенте """

        self.get_current_url()
        self.input_first_name('Aleksey')
        self.input_phone('+79112233445')
        self.click_payment_method()
        self.click_arrange_button()
        self.assert_word(self.get_main_word(), 'Введите код')
        self.get_screenshot()
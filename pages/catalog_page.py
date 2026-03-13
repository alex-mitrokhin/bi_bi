import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CatalogPage(Base):
    """ Класс содержащий локаторы и методы для страницы Каталог """


    # Locators

    brand_field = '(//input[@class ="input__field"])[2]'
    brand_checkbox = '//label[@name="brand"]'
    price_slider = '(//span[@class ="p-slider-handle _end-handler_8ya7z_27"])[1]'
    volume_slider = '(//span[@class="p-slider-handle _start-handler_8ya7z_26"])[2]'
    acea_checkbox = '(//label[@name="spetsifikatsii_acea"])[2]'
    vyazkost_checkbox = '(//label[@name="vyazkost"])[5]'
    production_header = '//a[.//span[text()="Выработка"]]'
    production_value = '(//label[@name="vyrabotka"])[3]'
    select_product = '//button[contains(@class, "_card-catalog__button_kx9qk_8")]'
    cart = '(//a[@class="nav__item"])[7]'
    go_cart = '//a[@class="app-button app-button--yellow"]'
    main_word = '//h1[@class="page__title"]'


    # Getters

    def get_brand_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_field)))

    def get_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_checkbox)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    def get_volume_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.volume_slider)))

    def get_acea_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.acea_checkbox)))

    def get_vyazkost_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vyazkost_checkbox)))

    def get_production_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.production_header)))

    def get_production_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.production_value)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))

    def get_move_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_go_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_cart)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def input_brand_field(self, word):
        self.get_brand_field().send_keys(word)
        print('Input brand oil')

    def click_brand_checkbox(self):
        self.get_brand_checkbox().click()
        print('Click brand checkbox')

    def move_price_slider(self):
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        actions.click_and_hold(self.get_price_slider()).move_by_offset(-80, 0).release().perform()

    def move_volume_slider(self):
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        actions.click_and_hold(self.get_volume_slider()).move_by_offset(80, 0).release().perform()

    def click_acea_checkbox(self):
        self.get_acea_checkbox().click()
        print('Click acea checkbox')

    def click_vyazkost_checkbox(self):
        self.get_vyazkost_checkbox().click()
        print('Click vyazkost checkbox')

    def click_production_header(self):
        self.get_production_header().click()
        print('Click production header')

    def click_production_value(self):
        self.get_production_value().click()
        print('Click production value')

    def click_select_product(self):
        # Скроллим наверх, где находится кнопка корзины
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)

        # Теперь получаем и кликаем по кнопке
        cart_button = self.get_cart()
        cart_button.click()
        print('Click cart button')

    def click_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_move_cart_button()).perform()

        # Ждем появления всплывающего окна
        time.sleep(1)

        go_to_cart = self.get_go_cart_button()
        go_to_cart.click()


    # Methods

    def filter_select_product(self):
        """ Выбор продукта по фильтрам """
        self.get_current_url()
        self.input_brand_field('Лукойл')
        self.click_brand_checkbox()
        self.move_price_slider()
        time.sleep(2)
        self.move_volume_slider()
        self.click_acea_checkbox()
        self.click_vyazkost_checkbox()
        self.click_production_header()
        self.click_production_value()
        self.click_select_product()
        self.click_cart()
        self.assert_word(self.get_main_word(), 'Корзина')
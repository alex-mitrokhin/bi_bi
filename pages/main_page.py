import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class MainPage(Base):
    """ Класс содержащий локаторы и методы для Главной страницы """

    url = 'https://www.bi-bi.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    popup = '//button[@class="app-button app-button--dark app-button--small confirm-city-popup__button"]'
    cookie = '//button[@class="cookie-button"]'
    menu = '//button[@class="app-button app-button--yellow header-sticky__catalog-btn"]'
    category_oil = '//span[@class="catalog-category__title" and contains(text(), "Масла")]'
    engine_oil = '//a[@class="category-block__link" and contains(text(), "Моторные")]'


    # Getters

    def get_popup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup)))

    def get_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_category_oil(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_oil)))

    def get_engine_oil(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.engine_oil)))


    # Actions

    def click_popup(self):
        self.get_popup().click()
        print('Click popup')

    def click_cookie(self):
        self.get_cookie().click()
        print('Click cookie')

    def click_menu(self):
        self.get_menu().click()
        print('Click menu')

    def click_category_oil(self):
        # Скроллим наверх, где находится кнопка корзины
        category_oil = self.get_category_oil()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", category_oil)
        time.sleep(1)

        # Теперь получаем и кликаем по кнопке
        category_oil.click()
        print('Click category oil')

    def click_engine_oil(self):
        self.get_engine_oil().click()
        print('Click engine oil')


    # Methods

    def select_engine_oil(self):
        """ Выбор пункта каталога 'Моторные масла' """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_popup()
        self.click_cookie()
        self.click_menu()
        self.click_category_oil()
        self.click_engine_oil()

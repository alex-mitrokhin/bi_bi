import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


def test_buy_product_1(set_group):
    """Тест покупки товара в интернет-магазине"""

    driver = webdriver.Chrome(service=Service('C:\\Users\\aleksey.mitrokhin\\PycharmProjects\\resourse\\chromedriver.exe'))
    print('Start Test 1')

    mp = MainPage(driver)
    mp.select_engine_oil()

    catp = CatalogPage(driver)
    catp.filter_select_product()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    print('Finish Test')
    time.sleep(2)
    driver.quit()
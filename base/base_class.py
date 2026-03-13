import datetime
import os


class Base():
    """Базовый класс, содержащий универсальные методы"""
    def __init__(self, driver):
        self.driver = driver

    """Method get url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, 'Значение текста не совпадает'
        print('Good value word')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot ' + now_date + '.png'

        current_dir = os.path.dirname(__file__)
        project_root = os.path.dirname(current_dir)
        screen_dir = os.path.join(project_root, 'screen')
        file_path = os.path.join(screen_dir, name_screenshot)
        self.driver.save_screenshot(file_path)
        print(f"Скриншот сохранен: {file_path}")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')
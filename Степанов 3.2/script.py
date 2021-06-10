import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(10)
        self.browser.get('http://suninjuly.github.io/registration1.html')
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        for elem in self.browser.find_elements_by_css_selector(".form-control"):
            elem.send_keys("f")
        self.browser.find_element_by_css_selector('button.btn.btn-default').click()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.browser.find_element_by_tag_name("h1").text

    def test_abs2(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(10)
        self.browser.get('http://suninjuly.github.io/registration2.html')
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        self.browser.find_element_by_class_name("form-control second").send_keys("f")
        for elem in self.browser.find_elements_by_css_selector(".form-control"):
            elem.send_keys("f")
        self.browser.find_element_by_css_selector('button.btn.btn-default').click()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.browser.find_element_by_tag_name("h1").text


if __name__ == "__main__":
    unittest.main()

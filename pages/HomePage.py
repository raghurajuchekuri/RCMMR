import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dynamicElementLocator(old, new, on_element=None):
    value = on_element[1].replace(old, new)
    ele_list = list(on_element)
    ele_list.pop(1)
    # on_element = self.browser.find_element(By.__str__(element.pop(0)), value)
    return By.__str__(ele_list.pop(0)), value


class HomePage:
    URL = "url is hidden"

    # Elements
    contact_us = (By.LINK_TEXT, 'Contact us')
    uncheck_all = (By.LINK_TEXT, 'Uncheck all')
    country_to_select = (By.XPATH, "//span[contains(@id,'REPLACE')]/parent::label/input")
    country_button = (By.XPATH, '//select[@id="SellingCountry"]/parent::td/button')
    country_names = (By.XPATH, "//input[contains(@id,'ui-multiselect-SellingCountry-option-')]/parent::label/span")

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.URL)

    def select_menu(self, menu_text):
        self.browser.find_element(*self.contact_us).click()

    def verify_page(self):
        pass

    def load(self):
        self.browser.get(self.URL)
        menu = self.browser.find_element(*HomePage.country_button).click()
        actions = ActionChains(self.browser)
        actions.click(menu)
        # self.country_to_select = HomePage.dynamicElementLocator(self, "OPTIONTEXT", "India", HomePage.country_to_select)
        options = self.browser.find_elements(*HomePage.country_names)
        result = list(filter(lambda item: (item.text == "India"), options))
        EC.visibility_of_element_located(result[0])
        result[0].click()
        # self.country_to_select = self.browser.find_element(
        #     dynamicElementLocator("REPLACE", "India", self.country_to_select))
        # if self.country_to_select.is_selected():
        #    self.country_to_select.click()


    def select_option_by_scroll(self, option_to_select, on_element=None):
        options = self.browser.find_elements(*on_element)
        result = list(filter(lambda item: (item.text == option_to_select), options))
        EC.visibility_of_element_located(result[0])
        result[0].click()

        print("Succeed Finally")

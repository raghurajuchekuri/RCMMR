from selenium.webdriver.common.by import By


class ContactUs:

    # Elements
    first_name = (By.ID, 'firstname')
    last_name = (By.ID, 'lastname')
    email = (By.ID, 'email')
    phone = (By.ID, 'phone')
    message = (By.NAME, 'message')

    def __init__(self, browser):
        self.browser = browser

    def enterCallBackDetails(self):
        self.browser.find_element(*self.first_name).send_keys("Chandraekar")
        self.browser.find_element(*self.last_name).send_keys("Ch")
        self.browser.find_element(*self.email).send_keys("cc.nist@gmail.com")
        self.browser.find_element(*self.phone).send_keys("8886140727")
        self.browser.find_element(*self.message).send_keys("hello message")
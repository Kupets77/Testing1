# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
driver = webdriver.Firefox()

class One(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_one(self):
        driver = self.driver
        self.open_catalog_page(driver)
        self.open_autorisation(driver)
        self.autorisation(driver, Group(username="ekylasov@gmail.com", password="2730443rusPERM"))
        self.output(driver)

    def output(self, driver):
        driver.find_element_by_xpath("//img[@alt='User avatar']").click()
        driver.find_element_by_xpath("//li[8]/button").click()
        driver.find_element_by_xpath("//footer[1]/button[1]").click()

    def autorisation(self, driver, group):
        driver.get("https://stepik.org/catalog?auth=login")
        driver.find_element_by_id("id_login_email").clear()
        driver.find_element_by_id("id_login_email").send_keys(group.username)
        driver.find_element_by_id("id_login_password").click()
        driver.find_element_by_id("id_login_password").clear()
        driver.find_element_by_id("id_login_password").send_keys(group.password)
        driver.find_element_by_xpath("//form[@id='login_form']/button").click()

    def open_autorisation(self, driver):
        driver.find_element_by_id("ember235").click()

    def open_catalog_page(self, driver):
        driver.get("https://stepik.org/catalog")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

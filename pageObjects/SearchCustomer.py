from selenium.webdriver.common.by import By
import time


class SearchCustomer:

    link_customerMenu_xpath = "//a[@href='#']/p[contains(text(), 'Customers')]"
    link_customerSubMenu_xpath = "//li/a[@href='/Admin/Customer/List']/p[contains(text(), 'Customers')]"
    textbox_searchEmail_id = "SearchEmail"
    textbox_searchFirstName_id = "SearchFirstName"
    button_searchCustomers_id = "search-customers"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customerMenu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customerSubMenu_xpath).click()

    def setSearchEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_searchEmail_id).send_keys(email)

    def clearSearchEmail(self):
        self.driver.find_element(By.ID, self.textbox_searchEmail_id).clear()

    def setFirstNameSearch(self, firstName):
        self.driver.find_element(By.ID, self.textbox_searchEmail_id).send_keys(firstName)

    def clickOnSearch(self):
        self.driver.find_element(By.ID, self.button_searchCustomers_id).click()
        time.sleep(4)

    def elementSearch(self, element):
        return self.driver.find_element(By.XPATH, f"//td[contains(text(), '{element}')]").text

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomer import AddCustomer
import string
import random


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen("Test_003_AddCustomer")

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add New Customer Test **********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickAddNew()

        self.logger.info("********** Starting Form Fill **********")
        email = random_generator() + "@gmail.com"
        self.addCust.setEmail(email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Leo")
        self.addCust.setLastName("Messi")
        self.addCust.setGender("Male")
        self.addCust.setDOB("3/21/1998")
        self.addCust.setCompany("MyCompany")
        self.addCust.setCustomerRoles("Vendors")
        self.addCust.selectVendorId("Vendor 1")
        self.addCust.setAdminComment("Its a MNC")

        self.addCust.clickSave()
        self.logger.info("********** Saving Customer Info **********")

        self.logger.info("********** Add Customer Validation Started **********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot("Screenshots/test_addCustomer.png")
            self.logger.error("********** Add Customer Test Passed **********")
            assert False

        self.logger.info("********** Ended Add New Customer Test **********")

        self.lp.clickLogout()


def random_generator():
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8))

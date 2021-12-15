import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomer import SearchCustomer


class Test_004_SearchCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen("Test_004_SearchCustomer")

    @pytest.mark.regression
    def test_searchCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Search Customer Test **********")

        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.clickOnCustomerMenu()
        self.searchCust.clickOnCustomerMenuItem()

        self.searchCust.setSearchEmail("brenda_lindgren@nopCommerce.com")
        self.searchCust.clickOnSearch()
        if self.searchCust.elementSearch("brenda") == "brenda_lindgren@nopCommerce.com":
            self.logger.info("Email Search Successful")
        else:
            self.logger.info("Email Search Failed")

        self.searchCust.clearSearchEmail()
        self.searchCust.setFirstNameSearch("Brenda")
        self.searchCust.clickOnSearch()
        if self.searchCust.elementSearch("Bren") == "Brenda":
            self.logger.info("First Name Search Successful")
        else:
            self.logger.info("Email Search Failed")

        self.logger.info("********** Ended Search Customer Test **********")
        self.lp.clickLogout()


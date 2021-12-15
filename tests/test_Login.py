import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen("Test_001_Login")

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Verifying HomePage Title Test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actualUrl = self.driver.title
        if actualUrl == "Your store. Login":
            self.logger.info("********** Home Page Title Test is passed **********")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_homePageTitle.png")
            self.logger.error("********** Home Page Title Test is failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginTest(self, setup):
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actualUrl = self.driver.title
        if actualUrl == "Dashboard / nopCommerce administration":
            self.logger.info("********** Login Test is passed **********")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.logger.error("********** Login Test is failed **********")
            assert False

        self.lp.clickLogout()


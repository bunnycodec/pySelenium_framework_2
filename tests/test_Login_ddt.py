import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = "TestData/LoginData.xlsx"
    logger = LogGen.logGen("Test_002_DDT_Login")

    @pytest.mark.regression
    def test_loginTest_ddt(self, setup):
        self.logger.info("********** Verifying test_loginTest_ddt **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = excelUtils.getRowCount(self.path, 'Sheet1')

        list_status = []
        for r in range(2, self.rows+1):
            self.user = excelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = excelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = excelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            actualUrl = self.driver.title
            if actualUrl == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("********** Login Test is Passed **********")
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********** Login Test is Failed **********")
                    list_status.append("Fail")
                self.lp.clickLogout()
            elif self.exp == "Pass":
                self.logger.info("********** Login Test is Failed **********")
                list_status.append("Fail")
            elif self.exp == "Fail":
                self.logger.info("********** Login Test is Passed **********")
                list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("********** Test_002_DDT_Login is Passed **********")
            assert True
        else:
            self.logger.info("********** Test_002_DDT_Login is Failed **********")
            assert False

        self.logger.info("********** Test_002_DDT_Login is Completed **********")

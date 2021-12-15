from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def setup(request):
    browserName = request.config.getoption("--browser")

    if browserName == "chrome":
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    elif browserName == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


############### Pytest HTML Reports ###############

# Hook for adding environment info to HTML report (You can add any number of metadata as per your wish)
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Bunny_Codec'


# Hook for deleting/modifying environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

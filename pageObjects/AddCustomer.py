import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    link_customerMenu_xpath = "//a[@href='#']/p[contains(text(), 'Customers')]"
    link_customerSubMenu_xpath = "//li/a[@href='/Admin/Customer/List']/p[contains(text(), 'Customers')]"
    btn_addNew_css = "a[class='btn btn-primary']"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstName_id = "FirstName"
    textbox_LastName_id = "LastName"
    radiobtn_genderMale_id = "Gender_Male"
    radiobtn_genderFemale_id = "Gender_Female"
    textbox_dob_id = "DateOfBirth"
    textbox_company_id = "Company"
    text_customerRole_xpath = "//label[@id='SelectedCustomerRoleIds_label']/../../../div[2]/div/div/div"
    select_vendorId_id = "VendorId"
    textarea_adminComment_id = "AdminComment"
    btn_save_name = "button[name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customerMenu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customerSubMenu_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_addNew_css).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.ID, self.textbox_firstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.textbox_LastName_id).send_keys(lastName)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.radiobtn_genderMale_id).click()
        else:
            self.driver.find_element(By.ID, self.radiobtn_genderFemale_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.textbox_dob_id).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(company)

    def setCustomerRoles(self, role):
        if role == "Guests":
            # A user can only select either guests or registered, if the user selects guests then delete registered
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[contains(text(), 'Regis')]/../span[2]/span").click()

        self.driver.find_element(By.XPATH, self.text_customerRole_xpath).click()
        role_path = "ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(), '"
        time.sleep(3)
        self.driver.find_element(By.XPATH, f"//{role_path}{role}')]").click()

    def selectVendorId(self, value):
        vendor = Select(self.driver.find_element(By.ID, self.select_vendorId_id))
        vendor.select_by_visible_text(value)

    def setAdminComment(self, adminComment):
        self.driver.find_element(By.ID, self.textarea_adminComment_id).send_keys(adminComment)

    def clickSave(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_save_name).click()
